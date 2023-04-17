# You are given an integer array nums and an array queries where queries[i] = [vali, indexi].

# For each query i, first, apply nums[indexi] = nums[indexi] + vali, then print the sum of the even values of nums.

# Return an integer array answer where answer[i] is the answer to the ith query.

 

# Example 1:

# Input: nums = [1,2,3,4], queries = [[1,0],[-3,1],[-4,0],[2,3]]
# Output: [8,6,2,4]
# Explanation: At the beginning, the array is [1,2,3,4].
# After adding 1 to nums[0], the array is [2,2,3,4], and the sum of even values is 2 + 2 + 4 = 8.
# After adding -3 to nums[1], the array is [2,-1,3,4], and the sum of even values is 2 + 4 = 6.
# After adding -4 to nums[0], the array is [-2,-1,3,4], and the sum of even values is -2 + 4 = 2.
# After adding 2 to nums[3], the array is [-2,-1,3,6], and the sum of even values is -2 + 6 = 4.
# Example 2:

# Input: nums = [1], queries = [[4,0]]
# Output: [0]
 

# Constraints:

# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# 1 <= queries.length <= 104
# -104 <= vali <= 104
# 0 <= indexi < nums.length


#TLE

class Solution(object):
    def sumEvenAfterQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        ans = []
        for i in range(len(queries)):
            nums[queries[i][1]] += queries[i][0]
            ans.append(sum(j for j in nums if j % 2 ==0))
        return ans

# Accepted
class Solution(object):
    def sumEvenAfterQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        even_sum = sum(value for value in nums if value % 2 == 0)
        ans = []
        for value, index in queries:
            if nums[index] % 2 == 0:
                even_sum -= nums[index]
            nums[index] += value
            if nums[index] % 2 == 0:
                even_sum += nums[index]
            ans.append(even_sum)
        return ans