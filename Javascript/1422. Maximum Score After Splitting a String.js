// Given a string s of zeros and ones, return the maximum score after splitting the string into two non-empty substrings (i.e. left substring and right substring).

// The score after splitting a string is the number of zeros in the left substring plus the number of ones in the right substring.

 

// Example 1:

// Input: s = "011101"
// Output: 5 
// Explanation: 
// All possible ways of splitting s into two non-empty substrings are:
// left = "0" and right = "11101", score = 1 + 4 = 5 
// left = "01" and right = "1101", score = 1 + 3 = 4 
// left = "011" and right = "101", score = 1 + 2 = 3 
// left = "0111" and right = "01", score = 1 + 1 = 2 
// left = "01110" and right = "1", score = 2 + 1 = 3
// Example 2:

// Input: s = "00111"
// Output: 5
// Explanation: When left = "00" and right = "111", we get the maximum score = 2 + 3 = 5
// Example 3:

// Input: s = "1111"
// // Output: 3

// Naive Solution

/**
 * @param {string} s
 * @return {number}
 */
var maxScore = function(s) {
    function countNums(string, num){
        let counter = 0
        if(num === 1){
            for (i of string){
                if(i === "1") counter += 1
            }
        }else{
            for (i of string){
                if(i === "0") counter += 1
            }
        }
        return counter
    }
    let max = 0
    for (let i = 0; i < s.length - 1; i++){
        let left = s.substring(0, i+1)
        let right = s.substring(i+1)
        max = Math.max(max, countNums(left, 0) + countNums(right, 1))
    }
    return max
};


// C2: Better Solution

/**
 * @param {string} s
 * @return {number}
 */
var maxScore = function(s) {
    let maxScore = 0
    let leftScore = 0
    let rightScore = s.split("").filter(x => x == "1").length
    for (let i = 0; i < s.length - 1; i++){
         s[i] === "0"? leftScore += 1: rightScore -= 1
         maxScore = Math.max(maxScore, leftScore + rightScore)
    }
    return maxScore
 };

 