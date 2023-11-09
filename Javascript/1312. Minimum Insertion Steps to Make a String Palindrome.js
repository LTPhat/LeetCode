// // HARD
// Given a string s. In one step you can insert any character at any index of the string.

// Return the minimum number of steps to make s palindrome.

// A Palindrome String is one that reads the same backward as well as forward.



// Example 1:

// Input: s = "zzazz"
// Output: 0
// Explanation: The string "zzazz" is already palindrome we do not need any insertions.
// Example 2:

// Input: s = "mbadm"
// Output: 2
// Explanation: String can be "mbdadbm" or "mdbabdm".
// Example 3:

// Input: s = "leetcode"
// Output: 5
// Explanation: Inserting 5 characters the string becomes "leetcodocteel".
 

// Constraints:

// 1 <= s.length <= 500
// s consists of lowercase English letters.

// Subproblem: Longest Palindrome Subsequence

// DP bottom-up approach

//  https://www.youtube.com/watch?v=_nCsPn7_OgI&t=331s

// DP equation: 

// // Every single character is a palindrome of length 1
// L(i, i) = 1 for all indexes i in given sequence

// // IF first and last characters are not same
// If (X[i] != X[j])  L(i, j) =  max{L(i + 1, j),L(i, j - 1)} 

// // If there are only 2 characters and both are same
// Else if (j == i + 1) L(i, j) = 2  

// // If there are more than two characters, and first and last 
// // characters are same
// Else L(i, j) =  L(i + 1, j - 1) + 2 
//


/**
 * @param {string} s
 * @return {number}
 */
var minInsertions = function(s) {
    function longestPalindromeSubsequence(s){
        const n = s.length
        dp = new Array(n).fill(0)
        for (let i = 0; i < n; i++){
            dp[i] = new Array(n).fill(0)
        }
        for (let i = 0; i < n; i++){
            dp[i][i] = 1
        }
        for (let subLength = 2; subLength <= n; subLength++){
            for(i = 0; i < n - subLength + 1; i++){
                let j = i + subLength - 1
                if(s[i] == s[j] && subLength == 2){
                    dp[i][j] = 2
                }else if(s[i] == s[j]){
                    dp[i][j] = 2 + dp[i+1][j-1]
                }else{
                    dp[i][j] = Math.max(dp[i][j-1], dp[i+1][j])
                }
            }
        }
        return dp[0][n-1]
    }
    return s.length - longestPalindromeSubsequence(s)
};