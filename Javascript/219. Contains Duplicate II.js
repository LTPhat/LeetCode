// Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

 

// Example 1:

// Input: nums = [1,2,3,1], k = 3
// Output: true
// Example 2:

// Input: nums = [1,0,1,1], k = 1
// Output: true
// Example 3:

// Input: nums = [1,2,3,1,2,3], k = 2
// Output: false

// My solution


/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */
var containsNearbyDuplicate = function(nums, k) {
    var hashmap = {}
    for (let i = 0; i < nums.length; i++){
        if (!hashmap[nums[i]]){
            hashmap[nums[i]] = [i]
        }else{
            hashmap[nums[i]].push(i)
        }
        if (hashmap[nums[i]].length > 1){
            for (let j = 0; j < hashmap[nums[i]].length; j++){
                if (Math.abs(hashmap[nums[i]][j] - hashmap[nums[i]][j + 1]) <= k)
                return true
            }
        }
    }
    return false
};

// Another solution

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */
var containsNearbyDuplicate = function(nums, k) {
    const map = new Map();
    for (let i = 0; i < nums.length; i++) {
        if (i - map.get(nums[i]) <= k) {
            return true;
        }
        map.set(nums[i], i);
    }
    return false;
};