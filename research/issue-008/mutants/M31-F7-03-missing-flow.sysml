// Clause 7.17.2 (SysML 2.0 Part 1, formal/2026-03-02, p.99), example verbatim;
// Scene, Picture, Focus and Shoot declarations supplied by the author.
// Provenance: KG-09-actions.PROVENANCE.md
package KG09Actions {
    private import ScalarValues::*;

    item def Scene;
    item def Picture;

    action def Focus {
        in scene : Scene;
        out image : Picture;
    }

    action def Shoot {
        in image : Picture;
        out picture : Picture;
    }

    action def TakePicture {
        in scene : Scene;
        out picture : Picture;

        bind focus.scene = scene;
        action focus : Focus { in scene; out image; }
        first focus then shoot;
        action shoot : Shoot { in image; out picture; }
        bind picture = focus.image;   // verbatim source reads focus.picture; see provenance
    }

    // Clause 7.17.3, Table 16 commentary (p.101), verbatim.
    action def ConcurrencyExample {
        fork fork1;
        first fork1 then action1;
        first fork1 then action2;

        action action1;
        action action2;

        join join1;
        first action1 then join1;
        first action2 then join1;

        first join1 then decision1;

        decide decision1;
        first decision1 then action3;
        first decision1 then action4;

        action action3;
        action action4;

        merge merge1;
        first action3 then merge1;
        first action4 then merge1;
    }
}
