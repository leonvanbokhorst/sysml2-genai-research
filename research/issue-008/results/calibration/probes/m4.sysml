package M4 {
    private import ScalarValues::*;
    metadata def abstract SafetyMetadata {
        attribute level : Integer;
    }
    part def BrakeSystem {
        @SafetyMetadata { level = 3; }
        attribute responseTime : Real;
    }
}
