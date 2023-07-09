// Given a binary array nums, you should delete one element from it.

// Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

 

// Example 1:

// Input: nums = [1,1,0,1]
// Output: 3
// Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
// Example 2:

// Input: nums = [0,1,1,1,0,1,1,0,1]
// Output: 5
// Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
// Example 3:

// Input: nums = [1,1,1]
// Output: 2
// Explanation: You must delete one element.


#include <iostream>
#include <unordered_map>
#include <algorithm>

int longestSubarray(std::vector<int>& nums) {
    std::unordered_map<int, int> map{{0, 0}, {1, 0}};
    int i = 0;
    int j = 0;
    int longest = std::numeric_limits<int>::min();
    while (j < nums.size()) {
        map[nums[j]] += 1;
        while (map[0] > 1) {
            map[nums[i]] -= 1;
            i += 1;
        }
        if (map[0] == 0) {
            longest = std::max(longest, map[1] - 1);
        } else {
            longest = std::max(longest, map[1]);
        }
        j += 1;
    }
    return longest == std::numeric_limits<int>::min() ? 0 : longest;
}