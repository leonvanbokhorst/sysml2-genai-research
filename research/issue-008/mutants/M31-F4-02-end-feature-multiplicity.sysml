// Clause 7.13.2 (SysML 2.0 Part 1, formal/2026-03-02, p.71), connection definition
// verbatim; Hub/Device and the usage in System supplied by the author.
// Provenance: KG-03-connections.PROVENANCE.md
package KG03Connections {
    private import ScalarValues::*;

    part def Hub;
    part def Device;

    connection def DeviceConnection {
        end part hub : Hub[2];
        end part device : Device;
        attribute bandwidth : Real;
    }

    part def System {
        part hub : Hub;
        part device : Device;
        connection link : DeviceConnection connect hub to device;
    }
}
