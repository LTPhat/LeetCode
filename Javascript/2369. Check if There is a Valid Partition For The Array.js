// You are given a 0-indexed integer array nums. You have to partition the array into one or more contiguous subarrays.

// We call a partition of the array valid if each of the obtained subarrays satisfies one of the following conditions:

// The subarray consists of exactly 2 equal elements. For example, the subarray [2,2] is good.
// The subarray consists of exactly 3 equal elements. For example, the subarray [4,4,4] is good.
// The subarray consists of exactly 3 consecutive increasing elements, that is, the difference between adjacent elements is 1. For example, the subarray [3,4,5] is good, but the subarray [1,3,5] is not.
// Return true if the array has at least one valid partition. Otherwise, return false.

// Initialization:

// Check the base case where the list has only one element. In this scenario, we can't create any valid subarray, so we return False.
// Initialize the dp array with the following values:
// dp[0] is True because an empty list is always valid.
// dp[1] is False initially.
// dp[2] checks if the first two numbers are identical.
// Iterate through the List:

// Start iterating from the third element (index = 2).
// For each number:
// Check if it matches the previous one and if dp[1] is True, indicating a valid partition up to this point.
// Check if it forms a triplet with the two preceding numbers that are identical and if dp[0] is True, maintaining the validity.
// Check if the current and the two preceding numbers form a sequence of three consecutive increasing numbers, and if dp[0] is True, keeping the partition valid.
// Slide the window forward by reassigning the values in the dp array.


/**
 * @param {number[]} nums
 * @return {boolean}
 */
var validPartition = function(nums) {
    let n = nums.length
    if (n <= 1) return false
    let curr_dp
    let dp = []
    dp.push(true)   // dp[0]
    dp.push(false)       // dp[1]
    if (nums[1] === nums[0]){
        dp.push(true)
    }else{
        dp.push(false)
    }
    for (let i = 2; i < n; i++){
        curr_dp = false
        if (nums[i] == nums[i-1] && dp[1])
            curr_dp = true
        if (nums[i] === nums[i-1] && nums[i-1] === nums[i-2] && dp[0])
            curr_dp = true
        if (nums[i] - nums[i-1] === 1 && nums[i-1] - nums[i-2] === 1 && dp[0])
            curr_dp = true
        dp[0] = dp[1]
        dp[1] = dp[2]
        dp[2] = curr_dp
    }
    return dp[2]
};