// You are given a 0-indexed integer array nums. For each index i (1 <= i <= nums.length - 2) the beauty of nums[i] equals:

// 2, if nums[j] < nums[i] < nums[k], for all 0 <= j < i and for all i < k <= nums.length - 1.
// 1, if nums[i - 1] < nums[i] < nums[i + 1], and the previous condition is not satisfied.
// 0, if none of the previous conditions holds.
// Return the sum of beauty of all nums[i] where 1 <= i <= nums.length - 2.

 

// Example 1:

// Input: nums = [1,2,3]
// Output: 2
// Explanation: For each index i in the range 1 <= i <= 1:
// - The beauty of nums[1] equals 2.
// Example 2:

// Input: nums = [2,4,6,4]
// Output: 1
// Explanation: For each index i in the range 1 <= i <= 2:
// - The beauty of nums[1] equals 1.
// - The beauty of nums[2] equals 0.
// Example 3:

// Input: nums = [3,2,1]
// Output: 0
// Explanation: For each index i in the range 1 <= i <= 1:
// - The beauty of nums[1] equals 0.

// leftArray[i]: Max of nums[:i+1]
// rightArray[i]: Min of nums[i+1:]
/**
 * @param {number[]} nums
 * @return {number}
 */
var sumOfBeauties = function(nums) {
    let sumBeauties = 0
    let n = nums.length
    let leftArray = new Array(n).fill(0)
    let rightArray = new Array(n).fill(Number.MAX_SAFE_INTEGER)
    leftArray[0] = nums[0]
    rightArray[n - 1] = nums[n - 1]
    for (let i = 1; i < n; i++){
        leftArray[i] = Math.max(leftArray[i - 1], nums[i])
    }
    for (let i = n - 2; i >= 0; i --){
        rightArray[i] = Math.min(rightArray[i + 1], nums[i])
    }
    for (let i = 0; i < n - 1; i++){
        if (leftArray[i - 1] < nums[i] && nums[i] < rightArray[i + 1]){
            sumBeauties += 2
        }else if (nums[i - 1] < nums[i] && nums[i] < nums[i + 1]){
            sumBeauties += 1
        }
    }
    return sumBeauties;
};