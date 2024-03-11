// You are given two strings order and s. All the characters of order are unique and were sorted in some custom order previously.

// Permute the characters of s so that they match the order that order was sorted. More specifically, if a character x occurs before a character y in order, then x should occur before y in the permuted string.

// Return any permutation of s that satisfies this property.

 

// Example 1:

// Input:  order = "cba", s = "abcd" 

// Output:  "cbad" 

// Explanation: "a", "b", "c" appear in order, so the order of "a", "b", "c" should be "c", "b", and "a".

// Since "d" does not appear in order, it can be at any position in the returned string. "dcba", "cdba", "cbda" are also valid outputs.

// Example 2:

// Input:  order = "bcafg", s = "abcd" 

// Output:  "bcad" 

// Explanation: The characters "b", "c", and "a" from order dictate the order for the characters in s. The character "d" in s does not appear in order, so its position is flexible.

// Following the order of appearance in order, "b", "c", and "a" from s should be arranged as "b", "c", "a". "d" can be placed at any position since it's not in order. The output "bcad" correctly follows this rule. Other arrangements like "bacd" or "bcda" would also be valid, as long as "b", "c", "a" maintain their order.



#include <iostream>
#include <unordered_map>

class Solution {
public:
    std::string customSortString(std::string order, std::string s) {
        std::unordered_map<char, int> counter;
        
        for (char i : s) {
            counter[i] = counter.find(i) != counter.end() ? counter[i] + 1 : 1;
        }

        std::string res = "";
        
        for (char ch : order) {
            if (counter.find(ch) != counter.end()) {
                res += std::string(counter[ch], ch);
                counter.erase(ch);
            }
        }

        for (const auto& pair : counter) {
            res += std::string(pair.second, pair.first);
        }

        return res;
    }
};