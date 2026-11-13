package M1 {
    private import ScalarValues::*;
    part def SafetyCase;
    part def BrakeSystem {
        @SafetyCase { }
        attribute responseTime : Real;
    }
}
