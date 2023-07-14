// Given an array nums of size n, return the majority element.

// The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

// Example 1:

// Input: nums = [3,2,3]
// Output: 3
// Example 2:

// Input: nums = [2,2,1,1,1,2,2]
// Output: 2
 

// Constraints:

// n == nums.length
// 1 <= n <= 5 * 104
// -109 <= nums[i] <= 109

/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
    var hash = {}
    for (let i = 0; i < nums.length; i++){
        if (!hash[nums[i]]){
            hash[nums[i]] = 1
        }else{
            hash[nums[i]] += 1
        }
        if(hash[nums[i]] > Math.floor(nums.length / 2)){
            return nums[i]
        }
    }
};





/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
    // var hash = {}
    // for (let i = 0; i < nums.length; i++){
    //     if (!hash[nums[i]]){
    //         hash[nums[i]] = 1
    //     }else{
    //         hash[nums[i]] += 1
    //     }
    //     if(hash[nums[i]] > Math.floor(nums.length / 2)){
    //         return nums[i]
    //     }
    // }

    
    //Boyer-Moore Majority Voting Algorithm
    let major_ele = nums[0]
    let major_fre = 1
    for (let i = 1; i < nums.length; i++){
        if (major_fre  === 0){
            major_ele = nums[i]
            major_fre = 1
        }else{
             if (nums[i] === major_ele){
                major_fre += 1
            }else{
                major_fre -= 1
            }
        }
    }
    return major_ele
};