// Given a 0-indexed integer array nums, determine whether there exist two subarrays of length 2 with equal sum. Note that the two subarrays must begin at different indices.

// Return true if these subarrays exist, and false otherwise.

// A subarray is a contiguous non-empty sequence of elements within an array.

 

// Example 1:

// Input: nums = [4,2,4]
// Output: true
// Explanation: The subarrays with elements [4,2] and [2,4] have the same sum of 6.
// Example 2:

// Input: nums = [1,2,3,4,5]
// Output: false
// Explanation: No two subarrays of size 2 have the same sum.
// Example 3:

// Input: nums = [0,0,0]
// Output: true
// Explanation: The subarrays [nums[0],nums[1]] and [nums[1],nums[2]] have the same sum of 0. 
// Note that even though the subarrays have the same content, the two subarrays are considered different because they are in different positions in the original array.

#include <unordered_set>
#include <vector>

bool findSubarrays(std::vector<int>& nums) {
    std::unordered_set<int> set;
    for (int i = 0; i < nums.size() - 1; i++) {
        std::vector<int> subArray(nums.begin() + i, nums.begin() + i + 2);
        int subSum = subArray[0] + subArray[1];
        if (set.count(subSum) > 0) {
            return true;
        }
        set.insert(subSum);
    }
    return false;
}