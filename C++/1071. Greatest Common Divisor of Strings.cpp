// For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).

// Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

 

// Example 1:

// Input: str1 = "ABCABC", str2 = "ABC"
// Output: "ABC"
// Example 2:

// Input: str1 = "ABABAB", str2 = "ABAB"
// Output: "AB"
#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;
class Solution {
public:
     string gcdOfStrings(string str1, string str2) {
        if (str1 + str2 != str2 + str1) {
            return "";
        }
        return findGCD(str1, str2);
    }

    private:
        string findGCD(string str1, string str2) {
            if (str1 == str2) {
                return str1;
            }
            else if (str1.length() > str2.length()) {
                return findGCD(str1.substr(str2.length()), str2);
            }
            else {
                return findGCD(str1, str2.substr(str1.length()));
            }
        }
};