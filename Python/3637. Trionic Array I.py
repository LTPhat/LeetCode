# You are given an integer array nums of length n.

# An array is trionic if there exist indices 0 < p < q < n − 1 such that:

# nums[0...p] is strictly increasing,
# nums[p...q] is strictly decreasing,
# nums[q...n − 1] is strictly increasing.
# Return true if nums is trionic, otherwise return false.

 

# Example 1:

# Input: nums = [1,3,5,4,2,6]

# Output: true

# Explanation:

# Pick p = 2, q = 4:

# nums[0...2] = [1, 3, 5] is strictly increasing (1 < 3 < 5).
# nums[2...4] = [5, 4, 2] is strictly decreasing (5 > 4 > 2).
# nums[4...5] = [2, 6] is strictly increasing (2 < 6).
# Example 2:

# Input: nums = [2,1,3]

# Output: false

# Explanation:

# There is no way to pick p and q to form the required three segments.

class Solution(object):
    def isTrionic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        turning = 0
        n = len(nums)
        diff = []
        for i in range(1, n):
            if nums[i] == nums[i - 1]:
                return False
            diff.append(nums[i] - nums[i - 1])

        signs = [1 if ele > 0 else -1 for ele in diff]
        if signs[0] != 1 or signs[-1] != 1:
            return False

        len_sign = len(signs)
        for i in range(1, len_sign):
            if signs[i] != signs[i - 1]:
                turning += 1
        
        return turning == 2