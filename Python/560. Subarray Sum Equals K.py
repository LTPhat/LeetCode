# # Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

# # A subarray is a contiguous non-empty sequence of elements within an array.

 

# # Example 1:

# # Input: nums = [1,1,1], k = 2
# # Output: 2
# # Example 2:

# # Input: nums = [1,2,3], k = 3
# # Output: 2
 

# # Constraints:

# # 1 <= nums.length <= 2 * 104
# # -1000 <= nums[i] <= 1000
# # -107 <= k <= 107

# The basic idea it to handle this problem with hashmap. The hashmap will store with the key being any particular sum, and the value being the number of time it has happened yet. Suppose we iterate the arrary from left to right and keep track of cumulative sum up to i in each position.


# If there is an increase of k in preSum[i], we can find preSum[j] = preSum[i] + k. (j > i)

# The origin problem find a subarry whose sum equals to k (preSum[j] - preSum[i]) can be changed to find a subarray whose sum equals to preSum[i] (preSum[j] - k)

class Solution(object):
    def subarraySum(self, nums, k):
        res = {}
        res[0] = 1 #We've already seen presum = 0 before iteration
        ans = 0
        presum = 0
        for i in nums:
            presum += i
            ans += res[presum-k]
            res[presum] += 1
        return ans