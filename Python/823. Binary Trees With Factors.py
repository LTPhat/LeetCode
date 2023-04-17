# Given an array of unique integers, arr, where each integer arr[i] is strictly greater than 1.

# We make a binary tree using these integers, and each number may be used for any number of times. Each non-leaf node's value should be equal to the product of the values of its children.

# Return the number of binary trees we can make. The answer may be too large so return the answer modulo 109 + 7.

 

# Example 1:

# Input: arr = [2,4]
# Output: 3
# Explanation: We can make these trees: [2], [4], [4, 2, 2]
# Example 2:

# Input: arr = [2,4,5,10]
# Output: 7
# Explanation: We can make these trees: [2], [4], [5], [10], [4, 2, 2], [10, 2, 5], [10, 5, 2].
 

# Constraints:

# 1 <= arr.length <= 1000
# 2 <= arr[i] <= 109
# All the values of arr are unique


class Solution(object):
    def numFactoredBinaryTrees(self, arr):
        arr.sort()
        #Initialize dict
        dp = {}
        for i in arr:
            dp[i] = 1
        for j, n in enumerate(arr):
            for k in range (j):
                if (n % arr[k] == 0) and (n // arr[k] in dp):
                    dp[n] += dp[arr[k]]*dp[n//arr[k]]
        module = 10**9 + 7
        return sum(dp.values()) % module
        
        