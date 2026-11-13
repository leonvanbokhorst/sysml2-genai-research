package P {
    private import ScalarValues::*;
    part def B { attribute p : Real; }
    part b : B;
    connection x connect b.p to b.p;
}
