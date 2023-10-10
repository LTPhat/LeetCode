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
 

// Kadane's Algorithm:
// If we have an array [2, 3, -1, -4]. A negative number -1 can turn the largest product of 2 * 3 = 6 into the smallest product which is 2 * 3 * -1 = -6. 
// But we need to keep track of it because the following -4 will turn the previous product into the largest which is 2 * 3 * -1 * -4 = 24. 
// Thus for this question, we not only have to keep track of the maximum product of the previous subarray, but also have to memoize the minimum product.
/**
 * @param {number[]} nums
 * @return {number}
 */
var maxProduct = function(nums) {
    let preMax = nums[0]
    let preMin = nums[0]
    let maxSoFar = nums[0]
    for (let i = 1; i < nums.length; i++){
        let currMin = Math.min(nums[i],  nums[i] * preMax, nums[i] * preMin)
        let currMax = Math.max(nums[i],  nums[i] * preMax, nums[i] * preMin)
        maxSoFar = Math.max(maxSoFar, currMax)
        preMax = currMax
        preMin = currMin
    }
    return maxSoFar
};