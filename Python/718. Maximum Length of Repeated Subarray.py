# # Given two integer arrays nums1 and nums2, return the maximum length of a subarray that appears in both arrays.Example 1:

# Input: nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
# Output: 3
# Explanation: The repeated subarray with maximum length is [3,2,1].
# Example 2:

# Input: nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
# Output: 5
 

# Constraints:

# 1 <= nums1.length, nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 100


import numpy as np
class Solution(object):
    def findLength(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        str_nums = "".join([chr(x) for x in nums2])
        str_ans  = ""
        ans = 0
        for i in nums1:
            str_ans += chr(i)
            if str_ans in str_nums:
                ans = max(ans, len(str_ans))
            else:
                str_ans = str_ans[1:]
        return len(str_ans)