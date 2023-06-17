// Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

// A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

// Example 1:

// Input: s = "abc", t = "ahbgdc"
// Output: true
// Example 2:

// Input: s = "axc", t = "ahbgdc"
// Output: false

 #include<iostream>
 #include<algorithm>
 #include<vector>
 using namespace std;

class Solution {
public:
    bool isSubsequence(string s, string t) {
    if (s.length() > t.length()) return false;
    int index = 0;
    for (char ch : t) {
        if (ch == s[index])
            index += 1;
    }
    return index == s.length();
    }
};