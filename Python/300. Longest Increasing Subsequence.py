# Given an integer array nums, return the length of the longest strictly increasing subsequence.

# A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

 

# Example 1:

# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
# Example 2:

# Input: nums = [0,1,0,3,2,3]
# Output: 4
# Example 3:

# Input: nums = [7,7,7,7,7,7,7]
# Output: 1

#O(n^2)
class Solution(object):
    def lengthOfLIS(self, nums):
        n = len(nums)
        dp = [1 for _ in range(n)]
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:          
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

#O(nlog(n))
class Solution:
    def lengthOfLIS(self, nums):
        # First use DP method
        piles = [nums[0]]
        n = len(nums)
        
        for i in range(1, n):
            target = nums[i]
            l = 0
            r = len(piles) 
            while(l < r):
                mid = l + (r - l)//2
                if piles[mid] < target:
                    l = mid + 1
                elif piles[mid] >= target:
                    r = mid
            if l == len(piles) :
                piles.append(target)
            else:
                piles[l] = target
        return len(piles)
        