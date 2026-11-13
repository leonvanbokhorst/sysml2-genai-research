// P02c — dataflow encoded so that its CONSEQUENCE is a checkable property: the sink's input is
// required to be 5.0 and the flow supplies it. Positive control for P02d.
package P02C {
    private import ScalarValues::*;

    action def Pipe {
        attribute observed : Real = 0.0;
        constraint wired { observed == 5.0 }

        action source { out v : Real; assign v := 5.0; }
        action sink { in u : Real; assign observed := u; }

        first source then sink;
        flow source.v to sink.u;
    }
}
