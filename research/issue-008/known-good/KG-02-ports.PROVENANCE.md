# KG-02-ports — provenance and validity argument

**Independence type:** S (specification example) with one author-added legal construct.
**Source:** SysML 2.0 Part 1, `formal/2026-03-02`, §7.12.2, p.62 (port definition/usage) and
§7.12.3, p.62 (conjugated port usage). PDF sha256 `46e6c047…a84a83a`.

**Quoted verbatim.**
```
port def FuelingPort {
    attribute flowRate : Real;
    out fuelOut : Fuel;
    in fuelReturn : Fuel;
}
part def FuelTank {
    port fuelOutPort : FuelingPort;
}
```
**Supplied by the author.** `item def Fuel;` (the fragment types two features with `Fuel` and never
declares it). The conjugated port usage `port fuelReturnPort : ~FuelingPort;`, which is the
specification's own §7.12.3 shorthand ("`port p : ~P;` is equivalent to `port p : P::'~P';`").
`private import ScalarValues::*;` for `Real`.

**Why it is believed valid.**
1. §7.12.2: "A port usage must only be defined by port definitions." `fuelOutPort : FuelingPort` —
   satisfied. §7.12.3: a conjugated port usage is a usage of the conjugated port definition
   `FuelingPort::'~FuelingPort'`, so `fuelReturnPort : ~FuelingPort` is a port usage of a port
   definition — satisfied.
2. §7.12.2: "All the features of a port definition or port usage, other than any nested port
   usages, must be referential (non-composite)." `flowRate : Real`, `out fuelOut : Fuel` and
   `in fuelReturn : Fuel` are the specification's own lines for this requirement; a directed
   feature of a port is referential by the specification's definition of the notation.
   **This is the one condition in this corpus that also appears in the prose-only register**
   (`validatePortDefinitionNestedUsagesNotComposite`, SysML §8.4.8.1, "missing_from_metamodel").
   A checker that implemented that prose-only rule strictly could disagree; if this instrument
   flags it, the finding belongs to the corpus and is reported, not silenced.
3. §7.12.2 default multiplicity of a port usage is 1..1 unless §7.6.3 conditions apply; none apply
   here and no explicit multiplicity is written.

**Author's uncertainty.** Whether `out fuelOut : Fuel` counts as a *composite* feature in the
abstract syntax depends on the direction/reference rules of §7.6.3. The specification uses this
exact line as its illustrative example, which is the strongest available evidence that it intends
the line to be legal.
