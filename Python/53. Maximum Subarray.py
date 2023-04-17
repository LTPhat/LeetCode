# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# A subarray is a contiguous part of an array.

 

# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Example 2:

# Input: nums = [1]
# Output: 1
# Example 3:

# Input: nums = [5,4,-1,7,8]
# Output: 23
 

# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# Time limit exceed
# class Solution(object):
#     def maxSubArray(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         ans = nums[0]
#         for i in range (len(nums)):
#             for j in range(1,len(nums)-i + 1):
#                 temp = nums[i:i+j]
#                 ans = max(ans,sum(temp))
#         return ans

# Dynamic Programing Solution
from sys import maxint
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        final_max  = -maxint 
        curr_max = 0
        for i in range(len(nums)):
            curr_max = max(nums[i],nums[i]+curr_max)
            final_max = max(final_max, curr_max)
        return final_max