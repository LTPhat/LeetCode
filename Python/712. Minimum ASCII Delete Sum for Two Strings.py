# Given two strings s1 and s2, return the lowest ASCII sum of deleted characters to make two strings equal.

 

# Example 1:

# Input: s1 = "sea", s2 = "eat"
# Output: 231
# Explanation: Deleting "s" from "sea" adds the ASCII value of "s" (115) to the sum.
# Deleting "t" from "eat" adds 116 to the sum.
# At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum possible to achieve this.
# Example 2:

# Input: s1 = "delete", s2 = "leet"
# Output: 403
# Explanation: Deleting "dee" from "delete" to turn the string into "let",
# adds 100[d] + 101[e] + 101[e] to the sum.
# Deleting "e" from "leet" adds 101[e] to the sum.
# At the end, both strings are equal to "let", and the answer is 100+101+101+101 = 403.
# If instead we turned both strings into "lee" or "eet", we would get answers of 433 or 417, which are higher.
 

class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        m, n = len(s2), len(s1)
        dp = [[0 for j in range(n + 1)] for i in range(0, m + 1)]
        for i in range(m):
            for j in range(n):
                if s1[j] == s2[i]:
                    dp[i + 1][j + 1] = dp[i][j] + ord(s1[j])
                else: 
                    dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])

        total_sum = sum(ord(j) for j in s1) + sum(ord(i) for i in s2)

        return total_sum - 2 * dp[m][n]

