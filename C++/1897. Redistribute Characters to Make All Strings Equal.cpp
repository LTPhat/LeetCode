// You are given an array of strings words (0-indexed).

// In one operation, pick two distinct indices i and j, where words[i] is a non-empty string, and move any character from words[i] to any position in words[j].

// Return true if you can make every string in words equal using any number of operations, and false otherwise.

 

// Example 1:

// Input: words = ["abc","aabc","bc"]
// Output: true
// Explanation: Move the first 'a' in words[1] to the front of words[2],
// to make words[1] = "abc" and words[2] = "abc".
// All the strings are now equal to "abc", so return true.
// Example 2:

// Input: words = ["ab","a"]
// Output: false
// Explanation: It is impossible to make all the strings equal using the operation.

class Solution {
public:
    bool makeEqual(vector<string>& words) {
        unordered_map <char, int> hashMap;
        for (auto &word: words){
            for(auto &a: word){
               hashMap[a] += 1;
            }
        }
        bool ans = true;
        for(auto item: hashMap){
            if (item.second % words.size() != 0){
                return false;
            }
        }
        return ans;
    }
};