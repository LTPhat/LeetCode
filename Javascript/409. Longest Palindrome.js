// Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

// Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

 

// Example 1:

// Input: s = "abccccdd"
// Output: 7
// Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
// Example 2:

// Input: s = "a"
// Output: 1
// Explanation: The longest palindrome that can be built is "a", whose length is 1.


/**
 * @param {string} s
 * @return {number}
 */
var longestPalindrome = function(s) {
    if (s.length == 1) return 1
    let pair = new Set()
    let ans = 0
    for (const i of s){
        if (pair.has(i)){
            ans += 2
            pair.delete(i)
        }else{
            pair.add(i)
        }
    }
    if (pair.size > 0){
        ans += 1
    }
    return ans
};