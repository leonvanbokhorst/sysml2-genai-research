// Clause 7.13.4 (SysML 2.0 Part 1, formal/2026-03-02, p.72), examples verbatim.
// Provenance: KG-04-featurevalues.PROVENANCE.md
package KG04FeatureValues {
    private import ScalarValues::*;
    private import SequenceFunctions::*;
    private import RealFunctions::*;

    attribute monthsInYear : Natural = 12;

    item def TestRecord {
        attribute scores[1] : Integer = (1, 2);
        derived attribute averageScore[1] : Rational = sum(scores)/size(scores);
        attribute cutoff : Integer default = 0.75 * averageScore;
    }

    item def TestWithCutoff :> TestRecord {
        attribute cutoff : Rational default = 0.75 * averageScore;
    }

    part def Counter {
        attribute count[1] : Natural := 0;
    }
}
