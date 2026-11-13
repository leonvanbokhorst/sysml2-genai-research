package GroundStationScheduling {
    private import ScalarValues::*;

    part def Antenna {
        attribute pointed : Boolean = false;
        attribute el : Real;
        attribute az : Real;
    }

    part def Transceiver {
        attribute receiving : Boolean = false;
    }

    part def Satellite {
        attribute visibilityStart : Real;
        attribute visibilityEnd : Real;
    }

    part def GroundStation {
        part antenna : Antenna;
        part transceiver : Transceiver;
        part satellites : Satellite[1..*];
    }

    requirement def InsideVisibilityWindow {
        subject station : GroundStation;
        doc /* A contact shall only be scheduled inside a satellite's visibility window and the
               antenna shall be pointed before the window opens. */
    }

    requirement insideWindow : InsideVisibilityWindow;
    satisfy insideWindow by station;

    action def ScheduleContact {
        in sat : Satellite;
        action checkWindow;
        action pointAntenna;
        action openLink;
        action closeLink;
        first checkWindow;
        then pointAntenna;
        then openLink;
        then closeLink;
    }

    part gs : GroundStation;
}
