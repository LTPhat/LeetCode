// You are given two strings s and t.

// String t is generated by random shuffling string s and then add one more letter at a random position.

// Return the letter that was added to t.

 

// Example 1:

// Input: s = "abcd", t = "abcde"
// Output: "e"
// Explanation: 'e' is the letter that was added.
// Example 2:

// Input: s = "", t = "y"
// Output: "y"


/**
 * @param {string} s
 * @param {string} t
 * @return {character}
 */
var findTheDifference = function(s, t) {
    function getFrequency(str) {
           const frequency = {};
           for (const char of str) {
               frequency[char] = (frequency[char] || 0) + 1;
           }
           return frequency;
       }

       const sFrequency = getFrequency(s);
       const tFrequency = getFrequency(t);

       for (const char in tFrequency) {
           if (sFrequency[char] !== tFrequency[char]) {
               return char;
       }
   }
};