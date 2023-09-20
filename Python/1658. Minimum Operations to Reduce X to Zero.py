# You are given an integer array nums and an integer x. In one operation, you can either remove the leftmost or the rightmost element from the array nums and subtract its value from x. Note that this modifies the array for future operations.

# Return the minimum number of operations to reduce x to exactly 0 if it is possible, otherwise, return -1.

 

# Example 1:

# Input: nums = [1,1,4,2,3], x = 5
# Output: 2
# Explanation: The optimal solution is to remove the last two elements to reduce x to zero.
# Example 2:

# Input: nums = [5,6,7,8,9], x = 4
# Output: -1
# Example 3:

# Input: nums = [3,2,20,1,1,3], x = 10
# Output: 5
# Explanation: The optimal solution is to remove the last three elements and the first two elements (5 operations in total) to reduce x to zero.


class Solution(object):
    def minOperations(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        def longestSubarraySumK(nums, k):
            left, right = 0, 0
            n = len(nums)
            curr_sum = nums[0]
            max_length = -1
            while right < n:
                while(curr_sum > k and left <= right):
                    curr_sum -= nums[left]
                    left += 1
                if (curr_sum == k):
                    max_length = max(max_length, right - left + 1)
                right += 1
                if right < n:
                    curr_sum += nums[right]
            return max_length
        if longestSubarraySumK(nums, sum(nums) - x) == -1:
            return -1
        return len(nums) - longestSubarraySumK(nums, sum(nums) - x)
        