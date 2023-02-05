// Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

// An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

// Example 1:

// Input: s = "cbaebabacd", p = "abc"
// Output: [0,6]
// Explanation:
// The substring with start index = 0 is "cba", which is an anagram of "abc".
// The substring with start index = 6 is "bac", which is an anagram of "abc".
// Example 2:

// Input: s = "abab", p = "ab"
// Output: [0,1,2]
// Explanation:
// The substring with start index = 0 is "ab", which is an anagram of "ab".
// The substring with start index = 1 is "ba", which is an anagram of "ab".
// The substring with start index = 2 is "ab", which is an anagram of "ab".


// SIMILAR PROBLEM OF 567 PERMUTAION OF STRING: HASH TABLE and SLICING WINDOW


/**
 * @param {string} s
 * @param {string} p
 * @return {number[]}
 */
var findAnagrams = function(s, p) {
    let res = []
    let mapS = {}
    let mapP = {}
    for (let i = 0; i < p.length; i++){
        if (!mapP[p[i]]) mapP[p[i]] = 0;
        mapP[p[i]] += 1;
        if (!mapS[s[i]]) mapS[s[i]] = 0;
        mapS[s[i]] += 1;
    }
    function check2map(map1, map2){
        for (let i in map1){
            if (!map1[i]) return false;
            if (map2[i] != map1[i]) return false;
        }
        return true;
    }
    for (let i = 0; i <= s.length - p.length; i++){
        if (check2map(mapP, mapS)) res.push(i);
        let next_char = i + p.length;
        if(!mapS[s[next_char]]) mapS[s[next_char]] = 0
        mapS[s[next_char]] += 1;
        mapS[s[i]] -= 1;
    }
    return res;
};