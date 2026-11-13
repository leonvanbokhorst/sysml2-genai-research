# KG-03-connections — provenance and validity argument

**Independence type:** S (specification example) plus an author-written usage.
**Source:** SysML 2.0 Part 1, `formal/2026-03-02`, §7.13.2, p.71.

**Quoted verbatim** (including the specification's own comment, whose second line is wrapped in
the PDF and is reflowed here):
```
// The related elements of this connection definition are the part definitions Hub and Device.
connection def DeviceConnection {
    end part hub : Hub;
    end part device : Device;
    attribute bandwidth : Real;
}
```
**Supplied by the author.** `part def Hub;`, `part def Device;` (referenced, not declared in the
fragment); the `System` part with two parts and one connection usage; the `package` wrapper and
the scalar-values import.

**Why it is believed valid.**
1. §7.13.2: "Unless it is abstract, a connection definition or usage must have at least two end
   features". Two, satisfied. "A binary connection … exactly two end features" — satisfied.
2. §7.13.2 with KerML `validateFeatureEndMultiplicity` (§8.3.3.3.4): "If a Feature has isEnd = true,
   then it must have multiplicity 1..1", and §7.13.2 states end features "must have multiplicity
   1..1" with an implicit 1..1 default. Neither end declares a multiplicity, so both take the
   implicit 1..1. Satisfied.
3. §7.13.2: "End features are always considered referential (non-composite)". Declared without
   `part`-composite semantics beyond the keyword used in the specification's own example.
4. The connection usage `connection link : DeviceConnection connect hub to device;` relates two
   features that both have `System` as featuring type, so KerML `checkConnectorTypeFeaturing`
   (§8.3.4.5.3, "each relatedFeature … must have each featuringType of the Connector as a direct or
   indirect featuringType") is satisfiable and satisfied.

**Author's uncertainty.** `connect A to B` is the succession/connection shorthand of §7.17.4; its
interaction with an explicitly typed connection usage is not spelled out in the clause I read.
Recorded as the weakest link in this model.
