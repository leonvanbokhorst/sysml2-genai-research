// Clause 7.12.2 (SysML 2.0 Part 1, formal/2026-03-02, p.62), example verbatim;
// item def Fuel supplied by the author. Provenance: KG-02-ports.PROVENANCE.md
package KG02Ports {
    private import ScalarValues::*;

    item def Fuel;

    port def FuelingPort {
        attribute flowRate : Real;
        out fuelOut : Fuel;
        in fuelReturn : Fuel;
    }

    part def FuelTank {
        part fuelOutPort : FuelingPort;
        // Clause 7.12.3: a conjugated port usage, legal notation for the
        // implicitly declared conjugated port definition FuelingPort::'~FuelingPort'.
        port fuelReturnPort : ~FuelingPort;
    }
}
