import sys
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = {}
        dp = [sys.maxsize] * (n+1)
        square = []
        for i in range(1, n+1):
            i_sq = pow(i, 2)
            if i_sq <= n:
                square.append(i_sq)
                dp[i_sq] = 1
            else: 
                for j in square:
                    if i < j: break
                    dp[i] = min(dp[i-j] + 1 , dp[i])
        return dp[n]
            