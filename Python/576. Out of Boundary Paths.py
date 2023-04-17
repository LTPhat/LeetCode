# There is an m x n grid with a ball. The ball is initially at the position [startRow, startColumn]. You are allowed to move the ball to one of the four adjacent cells in the grid (possibly out of the grid crossing the grid boundary). You can apply at most maxMove moves to the ball.

# Given the five integers m, n, maxMove, startRow, startColumn, return the number of paths to move the ball out of the grid boundary. Since the answer can be very large, return it modulo 109 + 7.

 

# Example 1:


# Input: m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0
# Output: 6
# Example 2:


# Input: m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1
# Output: 12
 

# Constraints:

# 1 <= m, n <= 50
# 0 <= maxMove <= 50
# 0 <= startRow < m
# 0 <= startColumn < n


class Solution(object):
    def findPaths(self, m, n, maxMove, startRow, startColumn):
        def dp(i, j, move):
            if (i,j,move) in memo:
                return memo[(i,j,move)]
            
            if i < 0 or j < 0 or i >= m or j >= n:
                return 1
            
            if move == 0:
                return 0
            
            ans = 0
            for d in directions:
                ni = i + d[0]
                nj = j + d[1]
                ans += dp(ni,nj,move-1)
            
            memo[(i,j,move)] = ans
            
            return ans
        
        memo = {}
        
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        mod = 10**9+7
        
        return dp(startRow, startColumn, maxMove) % mod