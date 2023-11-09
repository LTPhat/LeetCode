// Given a pattern and a string s, find if s follows the same pattern.

// Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

 

// Example 1:

// Input: pattern = "abba", s = "dog cat cat dog"
// Output: true
// Example 2:

// Input: pattern = "abba", s = "dog cat cat fish"
// Output: false
// Example 3:

// Input: pattern = "aaaa", s = "dog cat cat dog"
// Output: false


/**
 * @param {string} pattern
 * @param {string} s
 * @return {boolean}
 */
var wordPattern = function(pattern, s) {
    s_split = s.split(" ")
    if (pattern.length != s_split.length) return false
    var hash = {}
    var seen = new Set()
    for (let i = 0; i < pattern.length; i++){
        // If has new pattern but "seen" has its map
        if (!hash[pattern[i]] && seen.has(s_split[i])) {
            return false
        }
        // If has new pattern 
        if (!hash[pattern[i]]){
            hash[pattern[i]] = s_split[i]
        }else{
            if(hash[pattern[i]] != s_split[i])
            return false
        }
        seen.add(s_split[i])
    }
    return true
};