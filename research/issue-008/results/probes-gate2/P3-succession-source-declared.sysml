// Gate-2 probe (O5 control): the same text with `start` declared, so only the
// reference differs. Not a frozen mutant.
package P3SuccessionControl {
    private import ScalarValues::*;

    action def Cycle {
        action start;
        action sense;
        first start;
        then sense;
    }
}
