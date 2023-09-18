// We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.

// Given an integer array nums, return the length of its longest harmonious subsequence among all its possible subsequences.

// A subsequence of array is a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements.

 

// Example 1:

// Input: nums = [1,3,2,2,5,2,3,7]
// Output: 5
// Explanation: The longest harmonious subsequence is [3,2,2,2,3].
// Example 2:

// Input: nums = [1,2,3,4]
// Output: 2
// Example 3:

// Input: nums = [1,1,1,1]
// Output: 0
 

// Constraints:

// 1 <= nums.length <= 2 * 104
// -109 <= nums[i] <= 109
/**
 * 
 * 
 * @param {number[]} nums
 * @return {number}
 */
var findLHS = function(nums) {
    let counter = new Map();

        for (let i of nums) {
            counter.set(i, (counter.get(i) || 0) + 1);
        }

        let keys = Array.from(counter.keys()).sort((a, b) => a - b);

        if (keys.length === 1) {
            return 0;
        }

        let maxLength = 0;

        for (let i = 1; i < keys.length; i++) {
            if (Math.abs(keys[i] - keys[i - 1]) === 1) {
                maxLength = Math.max(maxLength, counter.get(keys[i]) + counter.get(keys[i - 1]));
            }
        }

        return maxLength;
};