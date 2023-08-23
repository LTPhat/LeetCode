// Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

// Return any possible rearrangement of s or return "" if not possible.

 

// Example 1:

// Input: s = "aab"
// Output: "aba"
// Example 2:

// Input: s = "aaab"
// Output: ""
 

// Constraints:

// 1 <= s.length <= 500
// s consists of lowercase English letters.

#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
#include <algorithm>


class Solution {
public:
    string reorganizeString(string s) {
        std::vector<int> ans(s.length(), 0);
        std::unordered_map<char, int> freMap;
        
        for (char c : s) {
            freMap[c] = freMap[c] + 1;
        }
        
        std::vector<std::pair<char, int>> sortedMap;
        for (const auto& entry : freMap) {
            sortedMap.emplace_back(entry.first, entry.second);
        }
        std::sort(sortedMap.begin(), sortedMap.end(), [](const auto& a, const auto& b) {
            return b.second < a.second;
        });
        
        if (sortedMap[0].second > (s.length() + 1) / 2) {
            return "";
        }
        
        int i = 0;
        for (const auto& entry : sortedMap) {
            char c = entry.first;
            int value = entry.second;
            for (int j = 0; j < value; j++) {
                if (i >= s.length()) {
                    i = 1;
                }
                ans[i] = c;
                i += 2;
            }
        }
        
        std::string result;
        for (int num : ans) {
            result += num;
        }
        
        return result;
    }
};