#!/usr/bin/env bash
# Run every capability probe against the pinned validator and preserve raw output.
#
# Rules this script enforces so the artifacts can be audited:
#   * each invocation writes one raw file containing: UTC timestamp, exact argv, tool version,
#     tool sha256, exit status, then unedited stdout and stderr;
#   * nothing is post-processed, filtered or trimmed — every line the tool emitted is kept;
#   * the exit status recorded is the tool's own, never a pipeline's.
#
# Usage: bash run-probes.sh        (from this directory, or from anywhere)

set -u

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO="$(cd "$HERE/../../../.." && pwd)"
SQL="$REPO/.tools/sysml"
RAW="$HERE/../raw"
RUNLOG="$HERE/../raw/RUNLOG.tsv"

if [ ! -x "$SQL" ]; then
  echo "pinned validator not found at $SQL" >&2
  exit 2
fi

mkdir -p "$RAW"

TOOL_SHA="$(shasum -a 256 "$SQL" | awk '{print $1}')"
TOOL_VER="$("$SQL" -version 2>/dev/null | head -1 | tr -s ' ')"

if [ ! -f "$RUNLOG" ]; then
  printf 'utc\tprobe\tinvocation_id\targv\texit\traw_file\n' > "$RUNLOG"
fi

# run <probe-basename> <invocation-id> <args...>
run() {
  local probe="$1"; shift
  local id="$1"; shift
  local file="$HERE/$probe.sysml"
  local out="$RAW/${probe}__${id}.txt"
  local utc; utc="$(date -u +%Y-%m-%dT%H:%M:%SZ)"

  if [ ! -f "$file" ]; then
    echo "missing probe file: $file" >&2
    return 2
  fi

  {
    echo "===== CRITIQUE CAPABILITY PROBE — RAW OUTPUT, UNEDITED ====="
    echo "utc:            $utc"
    echo "probe model:    probes/${probe}.sysml"
    echo "model sha256:   $(shasum -a 256 "$file" | awk '{print $1}')"
    echo "tool path:      .tools/sysml"
    echo "tool version:   $TOOL_VER"
    echo "tool sha256:    $TOOL_SHA"
    echo "argv:           sysml $* $probe.sysml"
    echo "----- stdout+stderr (verbatim; the sandbox record-cache notice is the tool's own stderr) -----"
  } > "$out"

  ( cd "$REPO" && "$SQL" "$@" "$file" ) >> "$out" 2>&1
  local rc=$?
  {
    echo "----- end of output -----"
    echo "exit:           $rc"
  } >> "$out"

  printf '%s\t%s\t%s\t%s\texit=%s\traw/%s\n' \
    "$utc" "$probe" "$id" "sysml $* $probe.sysml" "$rc" "${probe}__${id}.txt" >> "$RUNLOG"
  printf '%-46s %-22s exit=%s\n' "$probe" "$id" "$rc"
}

# ---- P00: pre-flight, the minimal decided/undecided pair -------------------------------------
for p in p00-smoke p00-smoke-bad; do
  run "$p" default-validate  -validate
  run "$p" instantiate-check -instantiate tank -validate=tank
done

# ---- P01: reachability of a terminal state / an unreachable state / no terminal state --------
for p in p01a-state-terminal-reachable p01b-state-terminal-unreachable p01c-state-nonterminating; do
  run "$p" default-validate      -validate
  run "$p" state-initial         -state Mission
  run "$p" state-advance-100     -state Mission -advance 100
  run "$p" state-advance-check   -state Mission -advance 100 -engine check
  run "$p" state-advance-explore -state Mission -advance 100 -schedule explore
  run "$p" self-check            -self-check
done

# ---- P02: missing flow between actions -------------------------------------------------------
for p in p02a-flow-present p02b-flow-missing; do
  run "$p" default-validate   -validate
  run "$p" action-run         -action TakePicture
  run "$p" action-check       -action TakePicture -engine check
  run "$p" action-explore     -action TakePicture -schedule explore
  run "$p" self-check         -self-check
done

# ---- P02c/P02d: dataflow whose consequence is encoded as a checkable property ----------------
for p in p02c-flow-wired p02d-flow-unwired; do
  run "$p" default-validate  -validate
  run "$p" action-run        -action Pipe
  run "$p" action-check      -action Pipe -engine check
  run "$p" engine-smt-prop   -action Pipe -engine smt -check-property wired
  run "$p" self-check        -self-check
done

# ---- P03: requirement satisfaction with a constraint ----------------------------------------
for p in p03a-req-constraint-holds p03b-req-constraint-violated; do
  run "$p" default-validate  -validate
  run "$p" satisfy-all       -satisfy
  run "$p" satisfy-json      -satisfy -json
  run "$p" instantiate-check -instantiate vehicle -validate=vehicle
  run "$p" requirement       -requirement vehicleMaximumMass
  run "$p" self-check        -self-check
done

# ---- P04: requirement satisfaction with prose only ------------------------------------------
run p04-req-prose-only default-validate   -validate
run p04-req-prose-only satisfy-all        -satisfy
run p04-req-prose-only satisfy-json       -satisfy -json
run p04-req-prose-only instantiate-check  -instantiate vehicle -validate=vehicle
run p04-req-prose-only requirement        -requirement maxMass
run p04-req-prose-only self-check         -self-check

# ---- P05: type conformance of an attribute value --------------------------------------------
for p in p05a-types-conformant p05b-types-nonconformant; do
  run "$p" default-validate  -validate
  run "$p" instantiate-check -instantiate device -validate=device
  run "$p" self-check        -self-check
done

# ---- P06: unit dimensional consistency ------------------------------------------------------
for p in p06a-units-consistent p06b-units-incommensurable; do
  run "$p" default-validate  -validate
  run "$p" instantiate-check -instantiate vehicle -validate=vehicle
  run "$p" self-check        -self-check
done

# ---- P07: contradictory assertions ----------------------------------------------------------
for p in p07a-assertions-consistent p07b-assertions-contradictory p07c-assertions-unbound; do
  run "$p" default-validate  -validate
  run "$p" instantiate-check -instantiate gauge -validate=gauge
  run "$p" instantiate-all   -instantiate gauge -validate=gauge -engine all
  run "$p" self-check        -self-check
done

# ---- P08: a property-checkable invariant over an execution ----------------------------------
for p in p08a-invariant-holds p08b-invariant-violated; do
  run "$p" default-validate          -validate
  run "$p" action-run                -action Seq
  run "$p" action-explore            -action Seq -schedule explore
  run "$p" engine-check-prop         -action Seq -engine check -check-property within15
  run "$p" engine-smt-prop           -action Seq -engine smt -check-property within15
  run "$p" engine-all-prop           -action Seq -engine all -check-property within15
  run "$p" engine-check-diverge      -action Seq -engine check -check-diverge x
  run "$p" self-check                -self-check
done

# ---- P11: a postcondition over a run's OUTPUT (verification case) ----------------------------
run p11-verification-case default-validate  -validate
run p11-verification-case analysis-over     -analysis over
run p11-verification-case analysis-under    -analysis under
run p11-verification-case analysis-arg-form -analysis "StopCheck(20.0)"
run p11-verification-case self-check        -self-check

# ---- P12: feature-value overriding at a second site (capability, not mutant validity) --------
run p12-fixed-binding-redefinition default-validate  -validate
run p12-fixed-binding-redefinition self-check        -self-check

# ---- P13: preserved dead ends (invocation forms that were refused) ---------------------------
run p13-dead-ends check-property-on-a-state  -state Mission -advance 10 -engine check -check-property Mission::done
run p13-dead-ends check-property-no-engine    -state Mission -advance 10 -check-property Mission::done
run p13-dead-ends observe-without-runs       -action Fill -observe level
run p13-dead-ends constraint-without-args    -instantiate tank -constraint Fits

# ---- P10: named-constraint evaluation and a part-level invariant -----------------------------
run p10-constraint-and-invariant default-validate        -validate
run p10-constraint-and-invariant constraint-on-object    -instantiate tank -constraint Fits
run p10-constraint-and-invariant constraint-args         -constraint "Fits(150.0, 100.0)"
run p10-constraint-and-invariant invariant-default       -validate=guardedTank
run p10-constraint-and-invariant invariant-instantiated  -instantiate guardedTank -validate=guardedTank
run p10-constraint-and-invariant self-check              -self-check

echo
echo "run log: $RUNLOG"

# ---- external cross-check: re-run one of Researcher B's own mutants, read-only -----------------
# Not a probe of mine: this re-runs B's frozen F5-01 mutant to establish whether
# `validateFeatureValueOverriding` is enforced by this binary at the site B tested. The file is
# read, never modified. Raw output is preserved here because the claim it tests is B's, not mine.
# usage: ext <id> <target> <args...>
ext() {
  local id="$1"; shift
  local target="$1"; shift
  local out="$RAW/EXTERNAL-issue-008__${id}.txt"
  local utc; utc="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  {
    echo "===== CRITIQUE CROSS-CHECK PROBE — RAW OUTPUT, UNEDITED ====="
    echo "utc:            $utc"
    echo "target model:   $target  (read-only; authored by Researcher B, issue #8)"
    echo "model sha256:   $(shasum -a 256 "$REPO/$target" | awk '{print $1}')"
    echo "tool version:   $TOOL_VER"
    echo "tool sha256:    $TOOL_SHA"
    echo "argv:           sysml $* $target"
    echo "----- stdout+stderr (verbatim) -----"
  } > "$out"
  ( cd "$REPO" && "$SQL" "$@" "$target" ) >> "$out" 2>&1
  local rc=$?
  { echo "----- end of output -----"; echo "exit:           $rc"; } >> "$out"
  printf '%s\t%s\t%s\t%s\texit=%s\traw/%s\n' \
    "$utc" "EXTERNAL:$target" "$id" "sysml $* $target" "$rc" "EXTERNAL-issue-008__${id}.txt" >> "$RUNLOG"
  printf '%-46s %-22s exit=%s\n' "EXTERNAL:$target" "$id" "$rc"
}

ext f5-01-default-validate research/issue-008/mutants/M31-F5-01-feature-value-overriding.sysml -validate
ext f5-01-base-validate    research/issue-008/known-good/KG-04-featurevalues.sysml -validate

# Re-run two of Researcher A's frozen probes (read-only) to check A's own capability claims.
ext a-probe07-reserved-keyword research/issue-007/detection/probes/probe07_reserved_keyword_name.sysml -validate
ext a-probe07-strict           research/issue-007/detection/probes/probe07_reserved_keyword_name.sysml -validate -strict
ext a-probe01-succession       research/issue-007/detection/probes/probe01_first_undefined_source.sysml -validate
