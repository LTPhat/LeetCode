// There is an integer array nums sorted in ascending order (with distinct values).

// Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

// Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

// You must write an algorithm with O(log n) runtime complexity.

 

// Example 1:

// Input: nums = [4,5,6,7,0,1,2], target = 0
// Output: 4
// Example 2:

// Input: nums = [4,5,6,7,0,1,2], target = 3
// Output: -1
// Example 3:

// Input: nums = [1], target = 0
// Output: -1
 

// Constraints:

// 1 <= nums.length <= 5000
// -104 <= nums[i] <= 104
// All values of nums are unique.
// nums is an ascending array that is possibly rotated.
// -104 <= target <= 104


// O(n) 
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function(nums, target) {
    return nums.indexOf(target);
};

// Case 1:
//   left  tar1     mid             tar2    right       => nums[left] < mid
//     4    5   6   7       0       1        2  

// Case 2:
//  left        tar3    mid         tar4     right      => nums[left] > mid
//  5           6       7           0     1   2

// O(logn)
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function(nums, target) {
    // return nums.indexOf(target);
    let left = 0
    let right = nums.length - 1
    while (left <= right){
        let mid = Math.floor((left + right) / 2)
        if (nums[mid] === target){
            return mid
        }else if (nums[mid] >= nums[left]){
            if (nums[left] <= target && target <= nums[mid]){       // tar1
                right = mid - 1
            }else{  
                left = mid + 1                                      // tar2
            }
        }else{
            if (nums[mid] <= target && target <= nums[right]){
                left = mid + 1                      // tar 4
            }else{
                right = mid - 1                     // tar 3
            }
        }
    }
    return -1 
};