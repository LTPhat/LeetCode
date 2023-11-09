// Given a string s consisting of words and spaces, return the length of the last word in the string.

// A word is a maximal 
// substring
//  consisting of non-space characters only.

 

// Example 1:

// Input: s = "Hello World"
// Output: 5
// Explanation: The last word is "World" with length 5.
// Example 2:

// Input: s = "   fly me   to   the moon  "
// Output: 4
// Explanation: The last word is "moon" with length 4.
// Example 3:

// Input: s = "luffy is still joyboy"
// Output: 6
// Explanation: The last word is "joyboy" with length 6.


// Solution 1:

/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function(s) {
    return s.trim().split(" ").reverse()[0].length
};

// Solution 2

/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function(s) {
    // return s.trim().split(" ").reverse()[0].length
    s = s.trim()
    let i = s.length - 1
    while(i >= 0 && s[i] != " "){
        i -= 1 // Find index of last word
    }
    let length = 0
    while(i < s.length - 1){
        length += 1
        i += 1
    }
    return length
};