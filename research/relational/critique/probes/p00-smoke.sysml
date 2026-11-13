package P00 {
    private import ScalarValues::*;

    part tank {
        attribute level : Real = 10.0;
        attribute capacity : Real = 100.0;
        assert constraint { level <= capacity }
    }
}
