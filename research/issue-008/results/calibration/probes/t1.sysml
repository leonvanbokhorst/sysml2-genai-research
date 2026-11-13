package T1 {
    private import ScalarValues::*;
    part def Vehicle {
        attribute mass : Real;
    }
    part v : Vehicle {
        attribute :>> mass = "heavy";
    }
}
