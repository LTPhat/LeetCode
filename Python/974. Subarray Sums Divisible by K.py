# # # Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.

# # # A subarray is a contiguous part of an array.

 

# # # Example 1:

# # # Input: nums = [4,5,0,-2,-3,1], k = 5
# # # Output: 7
# # # Explanation: There are 7 subarrays with a sum divisible by k = 5:
# # # [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
# # # Example 2:

# # # Input: nums = [5], k = 9
# # # Output: 0

# Algorithm: PREFIX SUM AND REMANDER FREQUENT DICT

# # If the prefixSum at i has a remainder of r, we just need to find how many of the previous prefixSum before i also has a remainder of r. This can be done using the frequency table to store the frequency of previous remainders.
# # When the previous prefixSum and the current prefixSum have the same remainder, it means the continues subarray in between has a sum which is divisable by k.

#  k = 3, nums = [1,2,3]
#                                     before       i=0,        i=1,        i=2
#     nums                         =                1,          2,          3
#     prefixSum                    =    0,          1,          3,          6
#     remainder of prefixSum       =    0,          1,          0,          0
#     frequency table of remainder =  {0:1}     {0:1,1:1}   {0:2,1:1}   {0:3,1:1}
#     res                          =    0,          0,          1,          2

from collections import defaultdict
class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        freq = defaultdict(int)
        freq[0] = 1
        res = 0
        prefix_sum = 0
        for i in nums:
            prefix_sum += i 
            remander = prefix_sum % k
            res += freq[remander]
            freq[remander] += 1
        return res

