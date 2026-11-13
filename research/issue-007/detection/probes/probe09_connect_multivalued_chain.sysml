package P {
    private import ScalarValues::*;
    part def B { port power; }
    part def C { part fleet : B[10]; part dock : B[2]; }
    part c : C;
    connection x connect c.fleet.power to c.dock.power;
}
