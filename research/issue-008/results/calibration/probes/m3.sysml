package M3 {
    private import ScalarValues::*;
    metadata def SafetyCritical {
        attribute level : Integer;
    }
    attribute responseTime : Real;
    @SafetyCritical { level = 3; }
}
