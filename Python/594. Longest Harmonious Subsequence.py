# We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.

# Given an integer array nums, return the length of its longest harmonious subsequence among all its possible subsequences.

# A subsequence of array is a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements.

 

# Example 1:

# Input: nums = [1,3,2,2,5,2,3,7]
# Output: 5
# Explanation: The longest harmonious subsequence is [3,2,2,2,3].
# Example 2:

# Input: nums = [1,2,3,4]
# Output: 2
# Example 3:

# Input: nums = [1,1,1,1]
# Output: 0
 

# Constraints:

# 1 <= nums.length <= 2 * 104
# -109 <= nums[i] <= 109

from collections import defaultdict

class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = defaultdict()
        for i in nums:
            counter[i] = counter.get(i, 0) + 1
        key = sorted(counter.keys())
        if len(key) == 1:
            return 0
        max_length = 0
        for i in range(1, len(key)):
            if key[i] - key[i -1] == 1:
                max_length = max(max_length, counter[key[i]] + counter[key[i - 1]])
        return max_length