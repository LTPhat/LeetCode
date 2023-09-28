# Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

# Return any array that satisfies this condition.

 

# Example 1:

# Input: nums = [3,1,2,4]
# Output: [2,4,3,1]
# Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
# Example 2:

# Input: nums = [0]
# Output: [0]
 

# Constraints:

# 1 <= nums.length <= 5000
# 0 <= nums[i] <= 5000


class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sort_nums = []
        index = []
        for i, num in enumerate(nums):
            if num % 2 == 0:
                sort_nums.append(num)
                index.append(i)

        for i in range(len(nums)):
            if i not in index:
                sort_nums.append(nums[i])

        return sort_nums
    
# Two pointer

class Solution(object):
    def sortArrayByParity(self, nums):
        i, j = 0, len(nums) - 1
        while i < j:
            while i < j and nums[i] % 2 == 0:
                i += 1
            while i < j and nums[j] % 2 == 1:
                j -= 1

            nums[i], nums[j] = nums[j], nums[i]
        return nums