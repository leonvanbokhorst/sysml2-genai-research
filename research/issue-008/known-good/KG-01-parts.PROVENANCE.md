# KG-01-parts — provenance and validity argument

**Independence type:** S (specification example).
**Source:** SysML 2.0 Part 1, `formal/2026-03-02`, §7.11.2, p.60. PDF sha256
`46e6c0476a6f1f34f367d57e039d56659bff75e41d2e4b3d37ca4cadea84a83a`; retrieved text
`/tmp/sysml/sysml-2.0-language.txt` (pdftotext), whose source PDF hash was verified against
`catalogue/README.md` §1.

**Quoted verbatim.** The `package` name apart, every declaration of `Vehicle` is the
specification's:
```
item def Person;
part def Vehicle {
    ref part driver[0..1] : Person;
    part engine : Engine;
    part wheels[4] : Wheel;
}
```
**Supplied by the author.** `part def Engine;` and `part def Wheel;` — the fragment references both
types without declaring them, so the model is not standalone as printed. `private import
ScalarValues::*;` (the fragment uses no scalar type; the import is inert and kept for consistency
with the other bases). The `package` wrapper.

**Why it is believed valid (constraint-level, not by validator acceptance).**
1. §7.11.2: "a part usage must only be defined by item definitions (including part definitions) or
   KerML structures". `engine : Engine` and `wheels : Wheel` are part usages typed by part
   definitions, a fortiori by item definitions. Satisfied.
2. `ref part driver[0..1] : Person`: a reference (non-composite) part usage typed by an item
   definition, exactly the specification's own line. §7.11.2 permits a part usage to be typed by an
   item definition.
3. `wheels[4]`: an explicit multiplicity on a feature. `4` is a `ScalarValues::Natural`
   (§8.3.4.11.2 requires the bound to be typed by `ScalarValues::Integer`) and is non-negative.
   Satisfied.
4. No connector, no redefinition, no metadata, no requirement: no constraint in the 623-row
   catalogue has a subject here beyond the generic ones (every Feature specializes `Base::things`,
   a `check…`, satisfied by construction since the tool derives it).
5. Nothing here is `isEnd`, so `validateFeatureEndMultiplicity` (KerML §8.3.3.3.4) does not apply.

**Known weakness.** A part with multiplicity 4 and no feature value is legal but semantically thin;
the model is a structural fragment, not an engineering model. That is intended: it is a base for
single-defect mutation, not a claim about good systems engineering.

## Author-supplied addition (added after the corpus was first validated)

`metadata def SafetyRelevant { attribute level : Integer; }` and the annotation
`@SafetyRelevant { level = 3; }` on `Vehicle` are **authored, not from the clause**. They exist so
that the metadata/annotation fault class (F8) has a base to mutate with a single-token edit, and so
that the known-good corpus contains at least one metadata application.

**Why the addition is believed well-formed.** §8.3.27.3 `checkMetadataUsageSpecialization` (MAY):
a metadata usage must specialize `Metadata::metadataItems`, which the library supplies implicitly
for a `metadata def`. KerML §8.3.4.12.3 `validateMetadataFeatureMetaclass` (SHOULD): a metadata
feature must have exactly one type that is a Metaclass — `SafetyRelevant` is a `metadata def`, which
is the notation for a metaclass in this language, and it is the only type. `validateMetadataFeatureMetaclassNotAbstract`:
`SafetyRelevant` is not abstract. `level = 3` binds an `Integer` feature to an integer literal.
