// P02d — the same action without the flow: the sink's input has no supplier, so `observed`
// cannot become 5.0. The property `wired` is the *authored* consequence of the missing flow.
package P02D {
    private import ScalarValues::*;

    action def Pipe {
        attribute observed : Real = 0.0;
        constraint wired { observed == 5.0 }

        action source { out v : Real; assign v := 5.0; }
        action sink { in u : Real; assign observed := u; }

        first source then sink;
    }
}
