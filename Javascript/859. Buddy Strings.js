// Given two strings s and goal, return true if you can swap two letters in s so the result is equal to goal, otherwise, return false.

// Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at s[i] and s[j].

// For example, swapping at indices 0 and 2 in "abcd" results in "cbad".
 

// Example 1:

// Input: s = "ab", goal = "ba"
// Output: true
// Explanation: You can swap s[0] = 'a' and s[1] = 'b' to get "ba", which is equal to goal.
// Example 2:

// Input: s = "ab", goal = "ab"
// Output: false
// Explanation: The only letters you can swap are s[0] = 'a' and s[1] = 'b', which results in "ba" != goal.
// Example 3:

// Input: s = "aa", goal = "aa"
// Output: true
// Explanation: You can swap s[0] = 'a' and s[1] = 'a' to get "aa", which is equal to goal.

/**
 * @param {string} s
 * @param {string} goal
 * @return {boolean}
 */
var buddyStrings = function(s, goal) {
    if (s.length != goal.length) return false
    if (s === goal){
        set = new Set(s.split(""))
        return set.size < s.length
    }

    diff_index = []
    for (let i = 0; i < s.length; i++){
        if(s[i] != goal[i]){
            diff_index.push(i)
        }
        if(diff_index.length > 2) return false
    }
    return diff_index.length === 2 && s[diff_index[0]] == goal[diff_index[1]] && s[diff_index[1]] == goal[diff_index[0]] 
};