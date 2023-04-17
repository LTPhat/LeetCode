# # Given an integer array nums, return all the different possible non-decreasing subsequences of the given array with at least two elements. You may return the answer in any order.

 

# # Example 1:

# # Input: nums = [4,6,7,7]
# # Output: [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]
# # Example 2:

# # Input: nums = [4,4,3,2,1]
# # Output: [[4,4]]

# #Algorithm: BACKTRACKING


# State is defined as the position i in nums we are currently visiting and the subsequence we have previously build.
# Now, at each position i, we have at most two choices:
# (1) Do not include nums[i] for the current subsequence we are building.
# (2) Include it in the current subsequence ONLY if it is the first element in the subsequence we are building, or it is greater than or equal to the last element in the subsequence we have already build (obey the non-decreasing property).
# We will use set to store the subsequences we built so that we don't have duplicates.
# We can translate the result from a set of tuples to a list of lists as the examples showed in the question, or just return it as set which is also acceptable by leetcode.


# Result display

# {(4, 6)}
# {(4, 6, 7), (4, 6)}
# {(4, 6, 7), (4, 6, 7, 7), (4, 6)}
# {(4, 6, 7), (4, 6, 7, 7), (4, 6)}
# {(4, 6, 7), (4, 6, 7, 7), (4, 6)}
# {(4, 6, 7), (4, 6, 7, 7), (4, 6)}
# {(4, 6, 7), (4, 6, 7, 7), (4, 6)}
# {(4, 6, 7), (4, 6, 7, 7), (4, 6), (4, 7)}
# {(4, 6), (4, 7, 7), (4, 6, 7), (4, 6, 7, 7), (4, 7)}
# {(4, 6), (4, 7, 7), (4, 6, 7), (4, 6, 7, 7), (4, 7)}
# {(4, 6), (4, 7, 7), (4, 6, 7), (4, 6, 7, 7), (4, 7)}
# {(4, 6), (4, 7, 7), (6, 7), (4, 6, 7), (4, 6, 7, 7), (4, 7)}
# {(4, 6), (4, 7, 7), (6, 7), (6, 7, 7), (4, 6, 7), (4, 6, 7, 7), (4, 7)}
# {(4, 6), (4, 7, 7), (6, 7), (6, 7, 7), (4, 6, 7), (4, 6, 7, 7), (4, 7)}
# {(4, 6), (4, 7, 7), (6, 7), (6, 7, 7), (4, 6, 7), (4, 6, 7, 7), (4, 7)}

# RES
# {(7, 7), (4, 6), (4, 7, 7), (6, 7), (6, 7, 7), (4, 6, 7), (4, 6, 7, 7), (4, 7)}


class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = set()
        def backtrack(i, subsequence):
            if len(subsequence) > 1:
                res.add(tuple(subsequence))
                print(res)
            if i== len(nums):
                return
            if not subsequence or nums[i] >= subsequence[-1]:
                backtrack(i+1, subsequence+[nums[i]])
            backtrack(i+1, subsequence)
        backtrack(0, [])
        return list(res)
        