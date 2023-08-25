// Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

// An interleaving of two strings s and t is a configuration where s and t are divided into n and m 
// substrings
//  respectively, such that:

// s = s1 + s2 + ... + sn
// t = t1 + t2 + ... + tm
// |n - m| <= 1
// The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
// Note: a + b is the concatenation of strings a and b.

 

// Example 1:


// Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
// Output: true
// Explanation: One way to obtain s3 is:
// Split s1 into s1 = "aa" + "bc" + "c", and s2 into s2 = "dbbc" + "a".
// Interleaving the two splits, we get "aa" + "dbbc" + "bc" + "a" + "c" = "aadbbcbcac".
// Since s3 can be obtained by interleaving s1 and s2, we return true.
// Example 2:

// Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
// Output: false
// Explanation: Notice how it is impossible to interleave s2 with any other string to obtain s3.
// Example 3:

// Input: s1 = "", s2 = "", s3 = ""
// Output: true
// Test case: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"

// s1	    0   1	2	3	4	5
// s2	_	_	a	a	b	c	c
// 0	_	T	T	T	F	F	F
// 1	d	F	F	T	T	F	F
// 2	b	F	F	T	T	T	F
// 3	b	F	F	T	F	T	F
// 4	c	F	F	T	T	T	F
// 5	a	F	F	F	F	T	T

/**
 * @param {string} s1
 * @param {string} s2
 * @param {string} s3
 * @return {boolean}
 */
var isInterleave = function(s1, s2, s3) {
    let m = s1.length
    let n = s2.length
    if (m + n !== s3.length) return false
    // dp [n x m]  s1 is row, s2 is col
    const dp = new Array(n + 1);
    for (let i = 0; i <= n; i++) {
        dp[i] = new Array(m + 1).fill(false);
    }
    dp[0][0] = true

    // Define first row and column dp
    for (let j = 1; j < m + 1; j++){
        dp[0][j] = dp[0][j - 1] && s1[j - 1] === s3[j - 1] 
    }
    for (let i = 1; i < n + 1; i++){
        dp[i][0] = dp[i - 1][0] && s2[i - 1] === s3[i - 1]
    }
    // Calculate dp[i][j], i, j >= 1
    for (let i = 1; i < n + 1; i++){
        for (let j = 1; j < m + 1; j++){
            dp[i][j] = (dp[i-1][j] && s2[i - 1] === s3[i + j - 1]) || (dp[i][j - 1] && s1[j - 1] === s3[i + j - 1])
        }
    }
    return dp[n][m]
};