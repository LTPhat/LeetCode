// Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

 

// Example 1:

// Input: n = 2
// Output: [0,1,1]
// Explanation:
// 0 --> 0
// 1 --> 1
// 2 --> 10
// Example 2:

// Input: n = 5
// Output: [0,1,1,2,1,2]
// Explanation:
// 0 --> 0
// 1 --> 1
// 2 --> 10
// 3 --> 11
// 4 --> 100
// 5 --> 101


/**
 * @param {number} n
 * @return {number[]}
 */
var countBits = function(n) {
    if (n == 0) return [0]
    let dp = Array(n + 1).fill(0)
    dp[0] = 0
    dp[1] = 1
    let count = 1
    let sub
    for (let i = 2; i <= n; i++){
        if (Math.pow(2, count) === i){
            sub = 0
            count += 1
        }
        dp[i] = dp[sub] + 1 
        sub += 1
    }
    return dp
};