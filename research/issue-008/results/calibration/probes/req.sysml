package Req {
    private import ScalarValues::*;
    part def Vehicle {
        attribute totalMass : Real;
    }
    requirement def MassLimit {
        doc /* The vehicle mass shall be at most 2000 kg. */
        attribute massActual : Real;
        attribute massRequired : Real;
        require constraint { massActual <= massRequired }
    }
    part vehicle : Vehicle {
        attribute totalMass = 1500.0;
    }
    requirement massLimit : MassLimit {
        subject v : Vehicle;
        attribute :>> massActual = 1500.0;
        attribute :>> massRequired = 2000.0;
    }
    satisfy massLimit by vehicle;
}
