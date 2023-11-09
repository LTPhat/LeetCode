// Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

// Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

 

// Example 1:

// Input: s = "abciiidef", k = 3
// Output: 3
// Explanation: The substring "iii" contains 3 vowel letters.
// Example 2:

// Input: s = "aeiou", k = 2
// Output: 2
// Explanation: Any substring of length 2 contains 2 vowels.
// Example 3:

// Input: s = "leetcode", k = 3
// Output: 2
// Explanation: "lee", "eet" and "ode" contain 2 vowels.
 

// Constraints:

// 1 <= s.length <= 105
// s consists of lowercase English letters.
// 1 <= k <= s.length

/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var maxVowels = function(s, k) {
    let max = -Number.MAX_SAFE_INTEGER
    let count = 0;
    const vowel = ['a', 'e', 'i', 'o', 'u'];
    for (let i = 0; i < s.length; i++){
        if (vowel.includes(s[i])){
            count += 1;
        }
        if (i > k - 1){
            count -= vowel.includes(s[i-k]);
        }
        max = Math.max(count, max);
    }
    return max;
};