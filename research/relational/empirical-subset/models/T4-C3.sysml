package WarehouseAgvFleetSystem {
    private import ScalarValues::*;

    part def Battery {
        attribute stateOfCharge : Real;
        attribute isCharging : Boolean = false;
        port power;
    }

    part def DockingStation {
        attribute isOccupied : Boolean = false;
        port power;
    }

    part def Agv {
        attribute hasAssignedJob : Boolean = false;
        part battery : Battery;
        port dockPort;
    }

    part def TransportJob {
        attribute jobId : String;
        attribute priority : Integer;
    }

    part def FleetController {
        attribute availableAgvCount : Integer;
        part vehicles : Agv[10];
        part stations : DockingStation[4];
    }

    part fleet : FleetController;

    requirement def ReturnBeforeLowChargeRequirement {
        subject f : FleetController;
        doc /* Each AGV shall dock at a charging station when its state of charge falls below 15%
               and shall not accept a new transport job while charging. */
        attribute returnThresholdPercent : Real = 15.0;
    }

    requirement returnBeforeLowCharge : ReturnBeforeLowChargeRequirement;
    satisfy returnBeforeLowCharge by fleet;

    action def AssignTransportJob {
        in job : TransportJob;
        in candidate : Agv;
        out assigned : Boolean;
        action checkCharge;
        action checkIdle;
        action dispatch;
        first checkCharge;
        then checkIdle;
        then dispatch;
    }

    connection batteryToDock connect fleet.vehicles.battery.power to fleet.stations.power;
}
