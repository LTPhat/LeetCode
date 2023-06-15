# You are given a sorted unique integer array nums.

# A range [a,b] is the set of all integers from a to b (inclusive).

# Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

# Each range [a,b] in the list should be output as:

# "a->b" if a != b
# "a" if a == b
 

# Example 1:

# Input: nums = [0,1,2,4,5,7]
# Output: ["0->2","4->5","7"]
# Explanation: The ranges are:
# [0,2] --> "0->2"
# [4,5] --> "4->5"
# [7,7] --> "7"
# Example 2:

# Input: nums = [0,2,3,4,6,8,9]
# Output: ["0","2->4","6","8->9"]
# Explanation: The ranges are:
# [0,0] --> "0"
# [2,4] --> "2->4"
# [6,6] --> "6"
# [8,9] --> "8->9"

class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums: 
            return 
        ans = []
        rangeList = [[] for i in range(0, len(nums))]
        index = 0
        for i in range(1, len(nums)):
            if nums[i] - 1 != nums[i - 1]:
                rangeList[index].append(nums[i - 1])
                index += 1
            else:
                rangeList[index].append(nums[i - 1])
        rangeList[index].append(nums[i])
        for item in rangeList:
            if not item:
                continue
            if (item[0] == item[-1]):
                ans.append("{}".format(item[0]))
            else:
                ans.append("{}->{}".format(item[0], item[-1]))
        return ans