// Given an integer array nums, find a 
// subarray
//  that has the largest product, and return the product.

// The test cases are generated so that the answer will fit in a 32-bit integer.

 

// Example 1:

// Input: nums = [2,3,-2,4]
// Output: 6
// Explanation: [2,3] has the largest product 6.
// Example 2:

// Input: nums = [-2,0,-1]
// Output: 0
// Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

#include <iostream>
#include <vector>
#include <algorithm>

int maxProduct(std::vector<int>& nums) {
    int preMax = nums[0];
    int preMin = nums[0];
    int maxSoFar = nums[0];
    
    for (int i = 1; i < nums.size(); i++) {
        int currMin = std::min(nums[i], std::min(nums[i] * preMax, nums[i] * preMin));
        int currMax = std::max(nums[i], std::max(nums[i] * preMax, nums[i] * preMin));
        maxSoFar = std::max(maxSoFar, currMax);
        preMax = currMax;
        preMin = currMin;
    }
    
    return maxSoFar;
}