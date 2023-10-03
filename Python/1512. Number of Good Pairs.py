# Given an array of integers nums, return the number of good pairs.

# A pair (i, j) is called good if nums[i] == nums[j] and i < j.

 

# Example 1:

# Input: nums = [1,2,3,1,1,3]
# Output: 4
# Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
# Example 2:

# Input: nums = [1,1,1,1]
# Output: 6
# Explanation: Each pair in the array are good.
# Example 3:

# Input: nums = [1,2,3]
# Output: 0
 

# Constraints:

# 1 <= nums.length <= 100
# 1 <= nums[i] <= 100


class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        fre = {}
        ans = 0
        for i in nums:
            fre[i] = fre.get(i, 0) + 1
        
        for i in fre.keys():
            val = fre.get(i)
            if val > 1:
                ans += val * (val - 1)/2
        return ans
        