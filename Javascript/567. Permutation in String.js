// Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

// In other words, return true if one of s1's permutations is the substring of s2.

 

// Example 1:

// Input: s1 = "ab", s2 = "eidbaooo"
// Output: true
// Explanation: s2 contains one permutation of s1 ("ba").
// Example 2:

// Input: s1 = "ab", s2 = "eidboaoo"
// Output: false
 

// Constraints:

// 1 <= s1.length, s2.length <= 104
// s1 and s2 consist of lowercase English letters.

// Algorithm: Hash table and Slicing Window

// console.log debug
// ex 1: s1 = "ab", s2 = "eidbaooo"
// Map1:
// { a: 1, b: 1 }
// Map2: 
// { e: 0, i: 1, d: 1 }
// //////
// Map1:
// { a: 1, b: 1 }
// Map2: 
// { e: 0, i: 0, d: 1, b: 1 }
// //////
// Map1:
// { a: 1, b: 1 }
// Map2: 
// { e: 0, i: 0, d: 0, b: 1, a: 1 }
// //////
// Checked


// ex2: 
// s1 = "abc"
// s2 = "cccccbabbbaaaa"


// Map1:
// { a: 1, b: 1, c: 1 }
// Map2: 
// { c: 3 }
// //////
// Map1:
// { a: 1, b: 1, c: 1 }
// Map2: 
// { c: 3 }
// //////
// Map1:
// { a: 1, b: 1, c: 1 }
// Map2: 
// { c: 2, b: 1 }
// //////
// Map1:
// { a: 1, b: 1, c: 1 }
// Map2: 
// { c: 1, b: 1, a: 1 }
// //////
// Checked






/**
 * @param {string} s1
 * @param {string} s2
 * @return {boolean}
 */
var checkInclusion = function(s1, s2) {
    let maps1 = {}
    let maps2 = {}

    // Create 2 map represent frequency of letters which length equal to map1.length
    for (let i = 0; i < s1.length; i ++){
        if (!maps1[s1[i]]) maps1[s1[i]] = 0;
        maps1[s1[i]] += 1;

        if (!maps2[s2[i]]) maps2[s2[i]] = 0;
        maps2[s2[i]] += 1;
    }
    // Check if all element in map1 belong to map2
    function check2map(map1, map2){
        for (let i in map1){
            if (!map2[i]) return false;
            if (map1[i] != map2[i]) return false;
        }
        return true;
    }
    for (let i = 0; i <= s2.length - s1.length; i++){
        if (check2map(maps1, maps2)) return true;
        let next_char = i + s1.length;
        if (!maps2[s2[next_char]]) maps2[s2[next_char]] = 0;
        maps2[s2[next_char]] += 1;
        maps2[s2[i]] -= 1;
    }
    return check2map(maps1, maps2);
};