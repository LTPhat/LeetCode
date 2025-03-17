# You are given an integer array nums consisting of 2 * n integers.

# You need to divide nums into n pairs such that:

# Each element belongs to exactly one pair.
# The elements present in a pair are equal.
# Return true if nums can be divided into n pairs, otherwise return false.

 

# Example 1:

# Input: nums = [3,2,3,2,2,2]
# Output: true
# Explanation: 
# There are 6 elements in nums, so they should be divided into 6 / 2 = 3 pairs.
# If nums is divided into the pairs (2, 2), (3, 3), and (2, 2), it will satisfy all the conditions.
# Example 2:

# Input: nums = [1,2,3,4]
# Output: false
# Explanation: 
# There is no way to divide nums into 4 / 2 = 2 pairs such that the pairs satisfy every condition.

class Solution(object):
    def divideArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if n % 2 != 0:
            return False
        
        count_map = {}
        for num in nums:
            count_map[num] = count_map.get(num, 0) + 1
        
        for key in count_map:
            if count_map.get(key) % 2 != 0:
                return False
        
        return True