// Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

// A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


 

// Example 1:

// Input: digits = "23"
// Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
// Example 2:

// Input: digits = ""
// Output: []
// Example 3:

// Input: digits = "2"
// Output: ["a","b","c"]


#include <vector>
#include <string>
#include <unordered_map>
using namespace std;


class Solution {
public:
    std::vector<std::string> letterCombinations(std::string digits) {
        std::unordered_map<char, std::string> digitToChar = {
            {'2', "abc"},
            {'3', "def"},
            {'4', "ghi"},
            {'5', "jkl"},
            {'6', "mno"},
            {'7', "pqrs"},
            {'8', "tuv"},
            {'9', "wxyz"}
        };

        std::vector<std::string> ans;
        std::string curr;

        // Backtracking function
        std::function<void(int)> backtrack = [&](int i) {
            if (curr.length() == digits.length()) {
                ans.push_back(curr);
                return;
            }

            for (char c : digitToChar[digits[i]]) {
                curr.push_back(c);
                backtrack(i + 1);
                curr.pop_back();
            }
        };

        if (!digits.empty()) {
            backtrack(0);
        }

        return ans;
    }
};