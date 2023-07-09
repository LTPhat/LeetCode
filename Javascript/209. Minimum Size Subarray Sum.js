// Given an array of positive integers nums and a positive integer target, return the minimal length of a 
// subarray
//  whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

// Example 1:

// Input: target = 7, nums = [2,3,1,2,4,3]
// Output: 2
// Explanation: The subarray [4,3] has the minimal length under the problem constraint.
// Example 2:

// Input: target = 4, nums = [1,4,4]
// Output: 1
// Example 3:

// Input: target = 11, nums = [1,1,1,1,1,1,1,1]
// Output: 0


// Sliding window

/**
 * @param {number} target
 * @param {number[]} nums
 * @return {number}
 */
var minSubArrayLen = function(target, nums) {
    let min_length = Number.MAX_SAFE_INTEGER
    let i = 0
    let j = 0
    let subarrSum = 0
    while (j < nums.length){
        subarrSum += nums[j]
        while(subarrSum >= target){
            min_length = Math.min(min_length, j - i + 1)
            subarrSum -= nums[i]
            i += 1
        }
        j += 1
    }
    return min_length === Number.MAX_SAFE_INTEGER ? 0: min_length
};