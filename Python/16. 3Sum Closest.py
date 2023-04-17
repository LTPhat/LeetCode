# Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

# Return the sum of the three integers.

# You may assume that each input would have exactly one solution.

 

# Example 1:

# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
# Example 2:

# Input: nums = [0,0,0], target = 1
# Output: 0
# Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
 

# Constraints:

# 3 <= nums.length <= 1000
# -1000 <= nums[i] <= 1000
# -104 <= target <= 104

# Algorithm:
# a, b, c is 3 number consider 3sum
# Temp ans is nums[0] + nums[1] + nums[2]

# Let a traverse through nums
#   With every a, using two pointer b = a + 1, c = nums[-1]
#   Calculate 3sum
#   If 3sum < target: move left_pointer (b) 1 step forward
#   If 3sum > target: move right_pointer (c) 1 step backward
#   If 3sum = target: Return target

# Calculate the difference with previous 3sum of previous loop to find 3sum closest to target

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort(reverse = False)
        ans = nums[0] + nums[1] + nums[2]
        for num in range(0, len(nums)-2):
            left = num + 1
            right = len(nums) - 1
            while left < right:
                three_sum = nums[num] + nums[left] + nums[right]
                if three_sum < target:
                    left += 1
                elif three_sum > target:
                    right -= 1
                else:
                    return target
            if abs(target - three_sum) < abs(target - ans):
                ans = three_sum
        return ans
                    
        