// You are given an integer array nums sorted in non-decreasing order.

// Build and return an integer array result with the same length as nums such that result[i] is equal to the summation of absolute differences between nums[i] and all the other elements in the array.

// In other words, result[i] is equal to sum(|nums[i]-nums[j]|) where 0 <= j < nums.length and j != i (0-indexed).

 

// Example 1:

// Input: nums = [2,3,5]
// Output: [4,3,5]
// Explanation: Assuming the arrays are 0-indexed, then
// result[0] = |2-2| + |2-3| + |2-5| = 0 + 1 + 3 = 4,
// result[1] = |3-2| + |3-3| + |3-5| = 1 + 0 + 2 = 3,
// result[2] = |5-2| + |5-3| + |5-5| = 3 + 2 + 0 = 5.
// Example 2:

// Input: nums = [1,4,6,8,10]
// Output: [24,15,13,15,21]


/**
 * @param {number[]} nums
 * @return {number[]}
 */
var getSumAbsoluteDifferences = function(nums) {
    const n = nums.length;
        const prefixSum = new Array(n).fill(0);
        prefixSum[0] = nums[0];

        for (let i = 1; i < n; i++) {
            prefixSum[i] = prefixSum[i - 1] + nums[i];
        }

        const ans = new Array(n).fill(0);
        let leftSum = 0;
        let rightSum = 0;

        for (let i = 0; i < n; i++) {
            leftSum = prefixSum[i] - nums[i];
            const leftEqualSum = i * nums[i];
            const leftDiff = leftEqualSum - leftSum;

            rightSum = prefixSum[n - 1] - prefixSum[i];
            const rightEqualSum = (n - i - 1) * nums[i];
            const rightDiff = rightSum - rightEqualSum;

            ans[i] = leftDiff + rightDiff;
        }

        return ans;
};