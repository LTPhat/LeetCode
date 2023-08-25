# Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

# An interleaving of two strings s and t is a configuration where they are divided into non-empty substrings such that:

# s = s1 + s2 + ... + sn
# t = t1 + t2 + ... + tm
# |n - m| <= 1
# The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
# Note: a + b is the concatenation of strings a and b.

 

# Example 1:


# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
# Output: true
# Example 2:

# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
# Output: false
# Example 3:

# Input: s1 = "", s2 = "", s3 = ""
# Output: true
 

# Constraints:

# 0 <= s1.length, s2.length <= 100
# 0 <= s3.length <= 200
# s1, s2, and s3 consist of lowercase English letters.

# Algorithm


#      0    1    2    3    4    5
#      d    b    b    c    a
# 0  a 

# 1  a 

# 2  b

# 3  b

# 4  c
# 5  


#Recursion solution
class Solution(object):
    def isInterleave(self, s1, s2, s3):
        dp = {}
        def grid(i,j):
            if i == len(s1) and j == len(s2):
                return True
            if (i,j) in dp:
                return dp[(i,j)]
            if i < len(s1) and s1[i] == s3[i+j] and grid(i+1,j)==True:
                return True
            if j < len(s2) and s2[j] == s3[i+j] and grid(i,j+1)==True:
                return True
            dp[(i,j)] = False
            return False
        if len(s1)+ len(s2) != len(s3):
            return False
        return grid(0,0)
        

# 2D Tabular Sol

class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        m = len(s1)
        n = len(s2)
        if m + n != len(s3):
            return False

        dp = [[False] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = True

        # Define first row and column dp
        for j in range(1, m + 1):
            dp[0][j] = dp[0][j - 1] and s1[j - 1] == s3[j - 1]

        for i in range(1, n + 1):
            dp[i][0] = dp[i - 1][0] and s2[i - 1] == s3[i - 1]

        # Calculate dp[i][j], i, j >= 1
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                dp[i][j] = (dp[i - 1][j] and s2[i - 1] == s3[i + j - 1]) or \
                        (dp[i][j - 1] and s1[j - 1] == s3[i + j - 1])

        return dp[n][m]