// Gate-2 probe (O3): reserved keyword used as an unquoted name. Not a frozen mutant.
package P1ReservedKeyword {
    private import ScalarValues::*;

    part def HeatPump {
        attribute outputPowerKw : Real;
        port return;
    }
}
