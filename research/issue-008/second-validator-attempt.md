# Second-instrument attempt (bounded, 20 minutes)

**Attempt window:** 2026-11-13T14:13:40Z – 2026-11-13T14:16Z (UTC). **Outcome: not obtained.**
**Consequence for the pilot:** every rate in the report is a one-instrument measurement. It
calibrates OpenSysML v0.12.1 against this corpus. It says nothing about "SysML v2 validators" in
general, and nothing about the OMG reference implementation's agreement or disagreement, because
that implementation was never run.

## What was tried, in order, with the exact result

### 1. Is there a Java runtime? → No.

```
$ java -version
The operation couldn't be completed. Unable to locate a Java Runtime.
Please visit http://www.java.com for information on installing Java.

$ /usr/libexec/java_home -V
The operation couldn't be completed. Unable to locate a Java Runtime.

$ ls -d /Library/Java/JavaVirtualMachines/* /opt/homebrew/opt/openjdk* /usr/local/opt/openjdk*
ls: /Library/Java/JavaVirtualMachines/*: No such file or directory
ls: /opt/homebrew/opt/openjdk*: No such file or directory
ls: /usr/local/opt/openjdk*: No such file or directory
```

`/usr/bin/java` exists but is the macOS first-run stub, not a runtime. This matches
`research/relational/TOOLING.md` §2. No build tool is present either: `which mvn gradle` returns
nothing.

**Classification of the failure: access/environment, not a technical defect of the artefact.** A
JVM is lawfully obtainable (Adoptium Temurin, Apache-2.0/GPL+CE builds are public); the blocker is
not permission, it is that the JVM is only the first of two blockers (see 3).

### 2. Does the pilot publish a CLI validator artefact? → No.

`https://api.github.com/repos/Systems-Modeling/SysML-v2-Pilot-Implementation/releases/latest`
(read-only, 2026-11-13T14:13:40Z) reports `tag_name: 2026-09.1`, `published_at:
2026-10-28T18:20:13Z`, with exactly these assets:

| asset | bytes |
|---|---:|
| `jupyter-sysml-kernel-0.63.1.zip` | 126,141,158 |
| `jupyterlab-sysml-0.63.1.tgz` | 5,080 |
| `Kernel_Data_Type_Library-1.1.0-dev.20260901.kpar` | 3,637 |
| `Kernel_Function_Library-1.1.0-dev.20260901.kpar` | 14,102 |
| `Kernel_Semantic_Library-1.1.0-dev.20260901.kpar` | 31,372 |
| `SysML_Analysis_Library-2.1.0-dev.20260901.kpar` | 5,438 |
| `SysML_Cause_and_Effect_Library-2.1.0-dev.20260901.kpar` | 2,620 |
| `SysML_Geometry_Library-2.1.0-dev.20260901.kpar` | 7,063 |
| `SysML_Metadata_Library-2.1.0-dev.20260901.kpar` | 4,019 |
| `SysML_Quantities_and_Units_Library-2.1.0-dev.20260901.kpar` | 152,715 |
| `SysML_Requirement_Derivation_Library-2.1.0-dev.20260901.kpar` | 2,171 |
| `SysML_Systems_Library-2.1.0-dev.20260901.kpar` | 25,470 |

There is no `sysml`, `validator`, `.jar` CLI bundle or GUI archive — confirming
`evidence/spec-tooling.md` §3.1 by direct observation of the asset list. The only executable
surface is the **Jupyter kernel**, which is a *library* surface: it would have to be driven through
magic commands whose validation verb is itself unverified (`evidence/spec-tooling.md` §3.3(e)
records that no file in the kernel's magic directory is named for validation and that whether a
`%validate` command exists is **NOT VERIFIED**).

### 3. Why the attempt stopped there

Obtaining a second instrument by this route needs, inside the 20-minute box: a JDK 21 download
and install; the 126 MB kernel zip; a Jupyter host (`jupyter_client` is not installed; no
`~/.local/share/jupyter`); discovery of the kernel's validation entry point by inspection of a JAR;
and then re-driving the 42-case matrix through a Jupyter message protocol instead of a CLI. Each
step is lawful; the chain is not achievable in the box, and a half-built harness would produce a
number nobody should trust. **The failure is therefore recorded as a not-obtained second
instrument, not forced.**

A JDK alone would not have been enough. That is the material point: the OMG reference implementation
has no standalone validator interface to invoke, which is itself evidence for the pilot's question
about what "available validator" means.

### 4. Alternatives considered and rejected, with the reason

| Candidate | Verdict | Reason |
|---|---|---|
| `DeciSym/sysmlv2-validator` | rejected | It is a CLI **wrapper around the pilot** (`evidence/spec-tooling.md` §6.2): same parser, same validator, and it needs Java 21 + Maven. A wrapper cannot serve as an independent instrument; two runs of one validator are not two witnesses. |
| `Fabi303/sysmlv2tool` | rejected | Second-hand report (OpenSysML differential) that the Tycho build fails (`No implementation for org.eclipse.tycho.core.resolver.MavenTargetLocationFactory`); not verified by me, and it would again wrap the pilot. |
| Syside (Sensmetry) | **access boundary** | Commercial; refuses to run without a licence key (`TOOLING.md` §3). Not bypassed, not attempted. |
| `cli_sysmlv2_syntaxchecker` (Télécom Paris) | not pursued | Appears in search results only; the GitLab host served an anti-bot interstitial to the earlier evidence pass. A syntax checker would also only exercise layer 1, which is the least interesting layer for this question. |

## Honest statement of what this costs the pilot

The report cannot separate three explanations for any miss it finds:
(a) the fault is beyond what SysML v2 validation can express;
(b) this instrument does not implement it;
(c) SysML v2 validators as a class do not implement it.
It can only say (b), plus (a) where the specification-oracle table shows no named constraint. Any
reading of the numbers as a property of "validators" is unsupported, and the report says so in its
first paragraph and in its limitations.
