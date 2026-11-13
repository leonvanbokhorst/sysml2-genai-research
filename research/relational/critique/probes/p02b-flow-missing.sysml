// P02b — the same action with the `flow` line deleted: `shoot.image` has no supplier.
// Property under test: missing flow between actions.
// Everything else is byte-identical to P02a apart from the package name and this comment.
package P02B {
    private import ScalarValues::*;

    item def Scene;
    item def Picture;

    action def Focus { in scene : Scene; out image : Picture; }
    action def Shoot { in image : Picture; out picture : Picture; }

    action def TakePicture {
        in scene : Scene;
        out picture : Picture;
        action focus : Focus { in scene; out image; }
        first focus then shoot;
        action shoot : Shoot { in image; out picture; }
        bind picture = focus.image;
    }
}
