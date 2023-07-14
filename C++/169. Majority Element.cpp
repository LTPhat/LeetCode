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

#include <vector>
#include <unordered_map>

int majorityElement(vector<int>& nums) {
    unordered_map<int, int> hash;
    int major_ele = nums[0];
    int major_fre = 1;

    for (int i = 0; i < nums.size(); i++) {
        if (hash.find(nums[i]) == hash.end()) {
            hash[nums[i]] = 1;
        } else {
            hash[nums[i]] += 1;
        }
        if (hash[nums[i]] > nums.size() / 2) {
            return nums[i];
        }
    }
    return major_ele;
}