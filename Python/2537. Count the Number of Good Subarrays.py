# Given an integer array nums and an integer k, return the number of good subarrays of nums.

# A subarray arr is good if there are at least k pairs of indices (i, j) such that i < j and arr[i] == arr[j].

# A subarray is a contiguous non-empty sequence of elements within an array.

 

# Example 1:

# Input: nums = [1,1,1,1,1], k = 10
# Output: 1
# Explanation: The only good subarray is the array nums itself.
# Example 2:

# Input: nums = [3,1,4,3,2,2,4], k = 2
# Output: 4
# Explanation: There are 4 different good subarrays:
# - [3,1,4,3,2,2] that has 2 pairs.
# - [3,1,4,3,2,2,4] that has 3 pairs.
# - [1,4,3,2,2,4] that has 2 pairs.
# - [4,3,2,2,4] that has 2 pairs.

from collections import defaultdict

class Solution(object):
    def countGood(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        left, right = 0, 0
        count = defaultdict(int)
        total_pairs = 0
        result = 0
        for right in range(n):
            # Find the first 'good' subarray
            total_pairs += count[nums[right]]
            count[nums[right]] += 1
            # Good subarray found --> sliding window
            while total_pairs >= k:
                result += n - right   # Subarray from left to {right + 1, ..., n} are also good
                count[nums[left]] -= 1 # Remove left-most element
                total_pairs -= count[nums[left]]
                left += 1       # Increase left pointer
        
        return result

