package M2 {
    private import ScalarValues::*;
    metadata def SafetyCritical {
        attribute level : Integer;
    }
    part def BrakeSystem {
        @SafetyCritical { levl = 3; }
        attribute responseTime : Real;
    }
}
