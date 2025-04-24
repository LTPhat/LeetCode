# You are given an array nums consisting of positive integers.

# We call a subarray of an array complete if the following condition is satisfied:

# The number of distinct elements in the subarray is equal to the number of distinct elements in the whole array.
# Return the number of complete subarrays.

# A subarray is a contiguous non-empty part of an array.

 

# Example 1:

# Input: nums = [1,3,1,2,2]
# Output: 4
# Explanation: The complete subarrays are the following: [1,3,1,2], [1,3,1,2,2], [3,1,2] and [3,1,2,2].
# Example 2:

# Input: nums = [5,5,5,5]
# Output: 10
# Explanation: The array consists only of the integer 5, so any subarray is complete. The number of subarrays that we can choose is 10.
 

# Constraints:

# 1 <= nums.length <= 1000
# 1 <= nums[i] <= 2000


class Solution(object):
    def countCompleteSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        n = len(nums)
        n_distinct = len(set(nums))
        mapping = {}
        left, right = 0, 0
        while left <= right and left < n:
            # Find the complete subarray window
            while len(mapping) < n_distinct and right < n:
                num_add = nums[right]
                mapping[nums[right]] = mapping.get(nums[right], 0) + 1
                right += 1
            if len(mapping) == n_distinct:
                # Subarray [left, right], [left, right + 1], ..., [left, n] are also valid
                result += n - right + 1
            
            # Decrease key of 'left' before moving next
            mapping[nums[left]] -= 1
            # Remove key with value of 0 in mapping
            if mapping[nums[left]] == 0:
                del mapping[nums[left]]
            left += 1       # Move next step of 'left'

        return result