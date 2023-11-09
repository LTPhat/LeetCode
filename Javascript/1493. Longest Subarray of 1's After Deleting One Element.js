// Given a binary array nums, you should delete one element from it.

// Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

 

// Example 1:

// Input: nums = [1,1,0,1]
// Output: 3
// Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
// Example 2:

// Input: nums = [0,1,1,1,0,1,1,0,1]
// Output: 5
// Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
// Example 3:

// Input: nums = [1,1,1]
// Output: 2
// Explanation: You must delete one element.

/**
 * @param {number[]} nums
 * @return {number}
 */
var longestSubarray = function(nums) {
    let map = {0: 0, 1: 0}
    let i = 0
    let j = 0
    let longest = Number.MIN_SAFE_INTEGER
    while(j < nums.length){
        map[nums[j].toString()] += 1
        // Sliding Window
        while(map['0'] > 1){
            map[nums[i].toString()] -= 1
            i += 1
        }
        if (map['0'] == 0){
            // No element 0, must delete one element 1
            longest = Math.max(longest, map['1'] - 1) 
        }else{
            longest = Math.max(longest, map['1'])
        }
        j += 1
    }
    return longest === Number.MIN_SAFE_INTEGER ? 0: longest
};