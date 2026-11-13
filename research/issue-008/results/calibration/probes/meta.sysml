package Meta {
    private import ScalarValues::*;
    metadata def SafetyCritical {
        attribute level : Integer;
    }
    part def BrakeSystem {
        @SafetyCritical { level = 3; }
        attribute responseTime : Real;
    }
}
