package Bad {
    private import ScalarValues::*;
    part def Vehicle {
        attribute mass : Real;
    }
    part v : Vehicle {
        attribute :>> mass = "heavy";
    }
    part w : Vehicle {
        attribute :>> mass = 10.0;
    }
    attribute :>> mass = 5.0;
}
