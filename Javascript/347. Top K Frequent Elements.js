// Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

// Example 1:

// Input: nums = [1,1,1,2,2,3], k = 2
// Output: [1,2]
// Example 2:

// Input: nums = [1], k = 1
// Output: [1]
 

// Constraints:

// 1 <= nums.length <= 105
// -104 <= nums[i] <= 104
// k is in the range [1, the number of unique elements in the array].
// It is guaranteed that the answer is unique.
 

// Using freqOrder to store the most frequent element in ascending order instead of sorting


/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function(nums, k) {
    let map = new Map();
    for (let num of nums){
        map.set(num, map.get(num) + 1 || 1);
    }

    let freqOrder = new Array();
    for (let i = 0; i < nums.length + 1; i++){
        freqOrder.push([])
    }
    for (const [key, val] of map){
        freqOrder[val].push(key);
    }
    
    let ans = [];
    for (let i = freqOrder.length - 1; i >= 0; i --){
        if (freqOrder[i].length){
            for (let item of freqOrder[i]){
                ans.push(item);
            }
        }
        if (ans.length == k){
            return ans
        }
    }
};