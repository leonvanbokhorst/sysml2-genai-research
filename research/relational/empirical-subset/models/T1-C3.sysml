package GreenhouseIrrigationSystem {
    private import ScalarValues::*;

    part def MoistureProbe {
        attribute reading : Real;
        attribute bed : String;
    }

    part def SolenoidValve {
        attribute isOpen : Boolean = false;
        port inlet;
        port outlet;
    }

    part def Pump {
        attribute isRunning : Boolean = false;
        attribute flowRate : Real;
        port outlet;
    }

    part def Bed {
        attribute moisturePercent : Real;
        part probe : MoistureProbe;
        part valve : SolenoidValve;
    }

    part def IrrigationController {
        part bedA : Bed;
        part bedB : Bed;
        part pump : Pump;
    }

    part greenhouse : IrrigationController;

    requirement def MoistureBandRequirement {
        subject controller : IrrigationController;
        doc /* Soil moisture shall be kept between 35% and 75% ... */
        attribute lowerBound : Real = 35.0;
        attribute upperBound : Real = 55.0;
        attribute cutOff : Real = 50.0;
    }

    requirement moistureBand : MoistureBandRequirement;

    satisfy moistureBand by greenhouse;

    action def IrrigationCycle {
        in bed : Bed;
        action sense {
            out moisture : Real;
        }
        action compare {
            in moisture : Real;
            out belowLower : Boolean;
        }
        action irrigate {
            out delivered : Boolean;
        }
        first sense;
        then compare;
        then irrigate;
    }

    connection pumpToBedA connect greenhouse.pump.outlet to greenhouse.bedA.valve.inlet;
    connection pumpToBedB connect greenhouse.pump.outlet to greenhouse.bedB.valve.inlet;
}
