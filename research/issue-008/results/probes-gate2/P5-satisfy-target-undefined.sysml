// Gate-2 probe (O5 contrast): dangling SATISFY TARGET, the site A's corpus exercises
// and which A reports as detected. Not a frozen mutant.
package P5SatisfyTarget {
    private import ScalarValues::*;

    requirement def Limit {
        doc /* The tank shall not overfill. */
    }
    requirement limit : Limit;
    satisfy limit by nosuchtank;
}
