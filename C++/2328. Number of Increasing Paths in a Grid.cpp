// You are given an m x n integer matrix grid, where you can move from a cell to any adjacent cell in all 4 directions.

// Return the number of strictly increasing paths in the grid such that you can start from any cell and end at any cell. Since the answer may be very large, return it modulo 109 + 7.

// Two paths are considered different if they do not have exactly the same sequence of visited cells.

 

// Example 1:


// Input: grid = [[1,1],[3,4]]
// Output: 8
// Explanation: The strictly increasing paths are:
// - Paths with length 1: [1], [1], [3], [4].
// - Paths with length 2: [1 -> 3], [1 -> 4], [3 -> 4].
// - Paths with length 3: [1 -> 3 -> 4].
// The total number of paths is 4 + 3 + 1 = 8.
// Example 2:

// Input: grid = [[1],[2]]
// Output: 3
// Explanation: The strictly increasing paths are:
// - Paths with length 1: [1], [2].
// - Paths with length 2: [1 -> 2].
// The total number of paths is 2 + 1 = 3.
#include<iostream>
#include<algorithm>
#include<math.h>
#include<vector>

using namespace std;


class Solution {
public:
    
    int Helper(vector<vector<int>>& grid, int i, int j, vector<vector<int>>& dp, int prev)
    {
        if(i<0 || j<0 || i>=grid.size() || j>=grid[0].size() || prev>=grid[i][j])
            return 0;
        
        if(dp[i][j]!=-1)
            return dp[i][j];
        
        int top =  Helper(grid,i-1,j,dp,grid[i][j]);
        int bottom =  Helper(grid,i+1,j,dp,grid[i][j]);
        int right = Helper(grid,i,j+1,dp,grid[i][j]);
        int left =  Helper(grid,i,j-1,dp,grid[i][j]);
        
        dp[i][j] = (1 + top + bottom + right + left)%1000000007; // it will give signed integer overflow run time error if you do not modulo at this point of code
        return dp[i][j];
    }
    int countPaths(vector<vector<int>>& grid) {
        
        int m = grid.size();
        int n = grid[0].size();
        if(m==1 && n==1)
            return 1;
        vector<vector<int> > dp(m,vector<int> (n,-1));
        
        int ans =0;
        for(int i=0;i<m;i++)
        {
            for(int j=0;j<n;j++)
            {
                if(dp[i][j]==-1)
                  ans = (ans + Helper(grid,i,j,dp,-1))%1000000007;
                else
                  ans = (ans + dp[i][j])%1000000007;
            }
        }
        
        return ans;
    }
};