# You are given an integer array nums of length n.

# A partition is defined as an index i where 0 <= i < n - 1, splitting the array into two non-empty subarrays such that:

# Left subarray contains indices [0, i].
# Right subarray contains indices [i + 1, n - 1].
# Return the number of partitions where the difference between the sum of the left and right subarrays is even.

 

# Example 1:

# Input: nums = [10,10,3,7,6]

# Output: 4

# Explanation:

# The 4 partitions are:

# [10], [10, 3, 7, 6] with a sum difference of 10 - 26 = -16, which is even.
# [10, 10], [3, 7, 6] with a sum difference of 20 - 16 = 4, which is even.
# [10, 10, 3], [7, 6] with a sum difference of 23 - 13 = 10, which is even.
# [10, 10, 3, 7], [6] with a sum difference of 30 - 6 = 24, which is even.
# Example 2:

# Input: nums = [1,2,2]

# Output: 0

# Explanation:

# No partition results in an even sum difference.

class Solution(object):
    def countPartitions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_sum = sum(nums)
        left_sum = 0
        n = len(nums)
        ans = 0
        for i in range(n - 1):
            left_sum += nums[i]
            right_sum = total_sum - left_sum
            if (left_sum - right_sum) % 2 == 0:
                ans += 1
        
        return ans