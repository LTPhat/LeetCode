// Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

 

// Example 1:

// Input: arr = [1,2,2,1,1,3]
// Output: true
// Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
// Example 2:

// Input: arr = [1,2]
// Output: false
// Example 3:

// Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
// Output: true
#include<iostream>
#include<algorithm>
#include<string>
#include<vector>
#include<unordered_map>
#include<unordered_set>


using namespace std;
class Solution {
public:
    bool uniqueOccurrences(vector<int>& arr) {
        std::unordered_map<int, int> hashmap;
        for (int i = 0; i < arr.size(); i++) {
            if (hashmap.count(arr[i]))
                hashmap[arr[i]] += 1;
            else
                hashmap[arr[i]] = 1;
        }
        
        std::unordered_set<int> valueSet;
        for (const auto& pair : hashmap) {
            if (valueSet.count(pair.second))
                return false;
            valueSet.insert(pair.second);
        }
        
        return true;
    }
};