// You are given a 0-indexed string s and a dictionary of words dictionary. You have to break s into one or more non-overlapping substrings such that each substring is present in dictionary. There may be some extra characters in s which are not present in any of the substrings.

// Return the minimum number of extra characters left over if you break up s optimally.

 

// Example 1:

// Input: s = "leetscode", dictionary = ["leet","code","leetcode"]
// Output: 1
// Explanation: We can break s in two substrings: "leet" from index 0 to 3 and "code" from index 5 to 8. There is only 1 unused character (at index 4), so we return 1.

// Example 2:

// Input: s = "sayhelloworld", dictionary = ["hello","world"]
// Output: 3
// Explanation: We can break s in two substrings: "hello" from index 3 to 7 and "world" from index 8 to 12. The characters at indices 0, 1, 2 are not used in any substring and thus are considered as extra characters. Hence, we return 3.
 

// Constraints:

// 1 <= s.length <= 50
// 1 <= dictionary.length <= 50
// 1 <= dictionary[i].length <= 50
// dictionary[i] and s consists of only lowercase English letters
// dictionary contains distinct words

/**
 * @param {string} s
 * @param {string[]} dictionary
 * @return {number}
 */
var minExtraChar = function(s, dictionary) {
    let n = s.length;
    const dict_set = new Set(dictionary);
    const memo = new Map();
    function dp(start){
        if (start === n){
            return 0;
        }
        if (memo.has(start)){
            return memo.get(start);
        }
        let ans = dp(start + 1) + 1;
        for (i = start; i < n; i++){
            const curr = s.slice(start, i + 1);
            if (dict_set.has(curr)){
                ans = Math.min(ans, dp(i + 1))
            }
        }
        memo.set(start, ans)
        return ans
    }
    return dp(0)
};