package AgvFleet {
    private import ScalarValues::*;

    part def Battery {
        attribute stateOfCharge : Real;
        attribute capacityKwh : Real;
        port power;
    }

    part def DockingStation {
        attribute isAvailable : Boolean = true;
        port power;
    }

    part def Agv {
        attribute isCharging : Boolean = false;
        attribute hasJob : Boolean = false;
        part battery : Battery;
        part dock : DockingStation;
    }

    part def FleetController {
        attribute availableAgvs : Integer;
        part fleet : Agv[10];
    }

    part controller : FleetController;

    requirement def ReturnBeforeLowCharge {
        doc /* Each AGV shall dock at a charging station when its state of charge falls below
               15% and shall not accept a new transport job while charging. */
        attribute chargeThresholdPercent : Real = 15.0;
    }

    requirement returnToDock : ReturnBeforeLowCharge;
    satisfy returnToDock by controller;

    action def AssignJob {
        in agv : Agv;
        in jobId : String;
        out assigned : Boolean;
        first checkCharge;
        then checkAvailability;
        then assign;
    }

    action def checkCharge;
    action def checkAvailability;
    action def assign;

    connection powerLink connect controller.fleet.battery.power to controller.fleet.dock.power;
}
