# KG-08-quantities — provenance and validity argument

**Independence type:** A (**authored pattern**, not quoted from the specification).
**Source:** authored by Researcher B, using the normative ISQ and SI model libraries named in SysML
2.0 Part 1 §9 and the quantity notation of §7.7 (attributes) and §7.13.4 (feature values).

**Authored content.** All of it: package wrapper, imports, the `Vehicle` part definition and its
four attributes. No line is quoted from a specification example. This is the corpus's weakest
independence type and is labelled accordingly.

**Why it is believed valid.**
1. Each attribute is a usage typed by a quantity definition from ISQ (`MassValue`, `LengthValue`,
   `SpeedValue`, `EnergyValue`), which are `AttributeDefinition`s in the normative model library, so
   `checkAttributeUsageSpecialization` (specialize `Base::dataValues`) and the ISQ typing are
   satisfied by construction.
2. Each quantity literal's unit is dimensionally consistent with its declared type: kg with
   `MassValue`, m with `LengthValue`, m/s with `SpeedValue`. The units `kg`, `m`, `m/s` are
   measurement references in SI. No catalogue constraint names dimension conformance; the
   validity argument here is library semantics, not an OCL constraint (recorded honestly — this is
   the F6 oracle gap showing up in the base corpus).
3. `0.5 * unladenMass * ratedSpeed * ratedSpeed` is dimensionally M·(L·T⁻¹)² = M·L²·T⁻², i.e.
   energy, matching `EnergyValue`. The arithmetic is written in the order that keeps every
   intermediate product dimensionally meaningful.
4. No feature name collides with a unit symbol (`overallLength`, `unladenMass`, `ratedSpeed`,
   `kineticEnergyAtRatedSpeed`). This is deliberate: during calibration, a local `attribute m`
   shadowed the metre unit and produced a spurious `quantity-unit` warning. Recorded in
   `results/calibration/PRE-FREEZE-CALIBRATION.md`.

**Author's uncertainty.** Whether `0.5` is admitted as a `Real` literal without a unit in a
quantity product; whether `EnergyValue` is the library's actual name (I did not read the ISQ library
text — it is embedded in the pinned binary, and I did not extract it). If an ISQ name is wrong, the
fault would show as `unresolved`, and the triage step would catch it as a confound (iii).
