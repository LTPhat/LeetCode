// Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

 

// Example 1:

// Input: num = 38
// Output: 2
// Explanation: The process is
// 38 --> 3 + 8 --> 11
// 11 --> 1 + 1 --> 2 
// Since 2 has only one digit, return it.
// Example 2:

// Input: num = 0
// Output: 0
 

// Constraints:

// 0 <= num <= 231 - 1
 

// Follow up: Could you do it without any loop/recursion in O(1) runtime?



// 1) Loop solution
/**
 * @param {number} num
 * @return {number}
 */
var addDigits = function(num) {
    while(num.toString().length > 1){
        num = num.toString().split("").reduce((sum, value) =>{
        return sum += Number(value)
        }, 0)
    }
    return num
};

// 2) O(1) runtime solution

/**
 * @param {number} num
 * @return {number}
 */
var addDigits = function(num) {
    if (num === 0) return 0
    if (num % 9 === 0) return 9
    return num % 9;
};