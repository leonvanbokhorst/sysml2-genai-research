package Hello {
    private import ScalarValues::*;
    part def Vehicle {
        attribute mass : Real;
    }
    part v : Vehicle {
        attribute :>> mass = 1200.0;
    }
}
