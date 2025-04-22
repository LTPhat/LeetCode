# Given a 0-indexed integer array nums of size n and two integers lower and upper, return the number of fair pairs.

# A pair (i, j) is fair if:

# 0 <= i < j < n, and
# lower <= nums[i] + nums[j] <= upper
 

# Example 1:

# Input: nums = [0,1,7,4,4,5], lower = 3, upper = 6
# Output: 6
# Explanation: There are 6 fair pairs: (0,3), (0,4), (0,5), (1,3), (1,4), and (1,5).
# Example 2:

# Input: nums = [1,7,9,2,5], lower = 11, upper = 11
# Output: 1
# Explanation: There is a single fair pair: (2,3).
 

# Constraints:

# 1 <= nums.length <= 105
# nums.length == n
# -109 <= nums[i] <= 109
# -109 <= lower <= upper <= 109

# TWO POINTERS SOLUTIONS
class Solution(object):
    def find_lowerbound(self, nums, value):
            n = len(nums)
            count = 0
            left, right = 0, n - 1
            while left < right:
                if nums[left] + nums[right] < value:
                    # Calculate n_pairs valid with 'left' is the first number 
                    n_pairs = right - (left + 1) + 1
                    count += n_pairs             
                    # Move to next element   
                    left += 1
                else:
                    right -= 1
            return count
    def countFairPairs(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        nums.sort()
        return self.find_lowerbound(nums, upper + 1) - self.find_lowerbound(nums, lower) 