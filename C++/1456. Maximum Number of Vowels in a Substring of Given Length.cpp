// Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

// Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

 

// Example 1:

// Input: s = "abciiidef", k = 3
// Output: 3
// Explanation: The substring "iii" contains 3 vowel letters.
// Example 2:

// Input: s = "aeiou", k = 2
// Output: 2
// Explanation: Any substring of length 2 contains 2 vowels.
// Example 3:

// Input: s = "leetcode", k = 3
// Output: 2
// Explanation: "lee", "eet" and "ode" contain 2 vowels.

#include<iostream>
 #include<algorithm>
 #include<vector>
 using namespace std;


class Solution {
public:
    int includes(char a){
        if (a == 'a' || a == 'e' ||a == 'i' || a == 'o' || a == 'u'){
            return 1;
        }
        return 0;
    }
    int maxVowels(string s, int k) {
        int maxVowel = INT_MIN;
        int count = 0;
        for (int i = 0; i < s.size(); i++){
            if(includes(s[i])){
                count += 1;
            }
            if (i > k - 1){
                count -= includes(s[i - k]);
            }
            maxVowel = max(maxVowel, count);
        }
        return maxVowel;
    }
};