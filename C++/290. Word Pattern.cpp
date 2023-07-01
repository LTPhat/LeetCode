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

#include <iostream>
#include <unordered_map>
#include <unordered_set>
#include <vector>
#include <sstream>

bool wordPattern(std::string pattern, std::string s) {
    std::vector<std::string> s_split;
    std::istringstream iss(s);
    std::string word;
    
    while (iss >> word) {
        s_split.push_back(word);
    }
    
    if (pattern.length() != s_split.size()) {
        return false;
    }
    
    std::unordered_map<char, std::string> hash;
    std::unordered_set<std::string> seen;
    
    for (int i = 0; i < pattern.length(); i++) {
        if (hash.find(pattern[i]) == hash.end() && seen.count(s_split[i])) {
            return false;
        }
        
        if (hash.find(pattern[i]) == hash.end()) {
            hash[pattern[i]] = s_split[i];
        } else {
            if (hash[pattern[i]] != s_split[i]) {
                return false;
            }
        }
        
        seen.insert(s_split[i]);
    }
    
    return true;
}