// Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

// An input string is valid if:

// Open brackets must be closed by the same type of brackets.
// Open brackets must be closed in the correct order.
// Every close bracket has a corresponding open bracket of the same type.
 

// Example 1:

// Input: s = "()"
// Output: true
// Example 2:

// Input: s = "()[]{}"
// Output: true
// Example 3:

// Input: s = "(]"
// Output: false

/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    let stack = [];
    for (let ch of s){
        switch (ch){
            case "(":
                stack.push(ch);
                break;
            case "[":
                stack.push(ch);
                break;
            case "{":
                stack.push(ch);
                break;
            case ")":
                if (stack.length == 0 || stack.pop() != "(")
                    return false;
                break;
            case "}":
                if (stack.length == 0 || stack.pop() != "{")
                return false;
                break;
            case "]":
                if (stack.length == 0 || stack.pop() != "[")
                return false;
                break;
        }
    }
    return stack.length === 0;
};