package GroundStation {
    private import ScalarValues::*;
    private import SI::*;

    part def Antenna {
        attribute azimuth : Real;
        attribute elevation : Real;
        attribute isPointed : Boolean = false;
    }

    part def Transceiver {
        attribute band : String = "S";
        attribute isTransmitting : Boolean = false;
    }

    part def Satellite {
        attribute noradId : Integer;
        attribute windowStart : Real;
        attribute windowEnd : Real;
    }

    part def GroundStation {
        part antenna : Antenna;
        part transceiver : Transceiver;
        part satellites : Satellite[1..*];
    }

    part station : GroundStation;

    requirement def ContactInsideWindow {
        doc /* A contact may only be scheduled inside a satellite's visibility window, and the
               antenna shall be pointed before the window opens. */
    }

    requirement windowObligation : ContactInsideWindow;
    satisfy windowObligation by station;

    action def ScheduleContact {
        in sat : Satellite;
        in requestedStart : Real;
        out scheduled : Boolean;
        action point;
        action checkWindow;
        action openLink;
        first checkWindow;
        then point;
        then openLink;
    }

    connection signalPath connect station.antenna to station.transceiver;
}
