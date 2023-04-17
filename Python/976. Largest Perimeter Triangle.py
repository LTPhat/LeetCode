# Given an integer array nums, return the largest perimeter of a triangle with a non-zero area, formed from three of these lengths. If it is impossible to form any triangle of a non-zero area, return 0.

 

# Example 1:

# Input: nums = [2,1,2]
# Output: 5
# Example 2:

# Input: nums = [1,2,1]
# Output: 0
 

# Constraints:

# 3 <= nums.length <= 104
# 1 <= nums[i] <= 106

# Sort reversely
# Take nums[0]; nums[1] are the two largest side
# Traverse third side from 2 to len(nums) choose i which satisfy triangle condition for side length
# If don't satisfy as the third --> Take a slide window 

class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort(reverse = True)
        first = 0
        second = 1
        for i in range(2, len(nums)):
            if nums[first] < nums[second] + nums[i]:
                return nums[first] + nums[second] + nums[i]
            first += 1
            second +=1
        return 0