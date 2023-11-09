// Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

// Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

// Example 1:

// Input: s = "leetcode", wordDict = ["leet","code"]
// Output: true
// Explanation: Return true because "leetcode" can be segmented as "leet code".
// Example 2:

// Input: s = "applepenapple", wordDict = ["apple","pen"]
// Output: true
// Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
// Note that you are allowed to reuse a dictionary word.
// Example 3:

// Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
// Output: false


// Initialization: Set dp[0] to true and the rest to false.
// Iteration: Iterate through the string from left to right, and for each position i, check the substrings ending at i to see if they are in the dictionary.
// Memoization: If a valid segmentation is found, update dp[i] to true.
// Result: The final result is stored in dp[n], where n is the length of the string.

/**
 * @param {string} s
 * @param {string[]} wordDict
 * @return {boolean}
 */
var wordBreak = function(s, wordDict) {
    let n = s.length
    let lengthWord = wordDict.map((word) => word.length)
    const max_len = Math.max(...lengthWord)
    let dp = Array(n + 1).fill(false)
    dp[0] = true
    for (let i = 1; i <= n; i++){
        for (let j = i - 1; j >= Math.max(i - max_len -1, -1); j--){
            if (dp[j] && wordDict.includes(s.slice(j, i))){
                dp[i] = true
                break
            }
        }
    }
    return dp[n]
};