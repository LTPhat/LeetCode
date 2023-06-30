// Given two strings s and t, determine if they are isomorphic.

// Two strings s and t are isomorphic if the characters in s can be replaced to get t.

// All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

// Example 1:

// Input: s = "egg", t = "add"
// Output: true
// Example 2:

// Input: s = "foo", t = "bar"
// Output: false
// Example 3:

// Input: s = "paper", t = "title"
// Output: true

#include <unordered_map>
#include <vector>
#include <string>

class Solution {
public:
    bool isIsomorphic(string s, string t) {
        if (s.length() != t.length())
        return false;

    std::unordered_map<char, char> charMap;
    std::unordered_map<char, bool> usedChars;

    for (int i = 0; i < s.length(); i++) {
        char c1 = s[i];
        char c2 = t[i];

        // If character c1 is already mapped but not to c2, return false
        if (charMap.count(c1) && charMap[c1] != c2)
            return false;

        // If character c1 is not mapped yet but c2 is already used, return false
        if (!charMap.count(c1) && usedChars.count(c2))
            return false;

        // Map character c1 to c2
        charMap[c1] = c2;
        usedChars[c2] = true;
    }

    return true;
    }
};