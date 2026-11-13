package P00B {
    private import ScalarValues::*;

    part tank {
        attribute level : Real = 150.0;
        attribute capacity : Real = 100.0;
        assert constraint { level <= capacity }
    }
}
