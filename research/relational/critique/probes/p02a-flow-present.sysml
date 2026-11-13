// P02a — base model: the subaction input is supplied by a flow.
// Property under test: missing flow between actions (a subaction input with no supplier).
package P02A {
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
        flow focus.image to shoot.image;
        action shoot : Shoot { in image; out picture; }
        bind picture = focus.image;
    }
}
