// Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

// Note that after backspacing an empty text, the text will continue empty.

 

// Example 1:

// Input: s = "ab#c", t = "ad#c"
// Output: true
// Explanation: Both s and t become "ac".
// Example 2:

// Input: s = "ab##", t = "c#d#"
// Output: true
// Explanation: Both s and t become "".
// Example 3:

// Input: s = "a#c", t = "b"
// Output: false
// Explanation: s becomes "c" while t becomes "b".



/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var backspaceCompare = function(s, t) {
    function getStack(s) {
            const stack = [];

            for (const i of s) {
                if (i === "#") {
                    if (stack.length === 0) {
                        continue;
                    } else {
                        stack.pop();
                    }
                } else {
                    stack.push(i);
                }
            }
            return stack;
        }

        const stackS = getStack(s);
        const stackT = getStack(t);

        if (stackS.length !== stackT.length) {
            return false;
        }

        for (let i = 0; i < stackS.length; i++) {
            if (stackS[i] !== stackT[i]) {
                return false;
            }
        }
        return true;
};