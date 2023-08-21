// Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

 

// Example 1:

// Input: s = "abab"
// Output: true
// Explanation: It is the substring "ab" twice.
// Example 2:

// Input: s = "aba"
// Output: false
// Example 3:

// Input: s = "abcabcabcabc"
// Output: true
// Explanation: It is the substring "abc" four times or the substring "abcabc" twice.
 

// Constraints:

// 1 <= s.length <= 104
// s consists of lowercase English letters.


/**
 * @param {string} s
 * @return {boolean}
 */
var repeatedSubstringPattern = function(s) {
    let n = s.length
    if (s.length === 1) return false
    for (let i = 0; i < n / 2 + 1; i++){
        if (n % i === 0){
            substr = s.slice(0, i)
            if (substr.repeat(Math.floor(n / i)) === s){
                return true
            }
        }
    }
    return false
};