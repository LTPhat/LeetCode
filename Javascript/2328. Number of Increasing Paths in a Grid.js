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

// -> Initialize a 2D vector 'dp' of size 'n' by 'm', where 'n' represents the number of rows and 'm' represents the number of columns in the grid.
// -> Check for all possible increasing paths for each element one by one.
// -> Initialize the previous value 'prev' as -1, assuming there are no negative values in the array, and make a recursive call.
// -> Check if the indexes are valid and if the current element is greater than the previous one.
// -> If we have already counted the paths going via current elements, then retrieve the data from the dp table.
// -> Increment the count by 1 each time if the curr element is greater than the previous one, as we can start from any cell and end at any cell according to the given question. Then, proceed in all four directions by making a recursive call.
// -> Return the count while storing it in the 'dp' table.


var countPaths = function(grid) {
    let mod = Math.pow(10, 9) + 7;
    let result = 0;
    let rows = grid.length, columns = grid[0].length;
    let dp = Array(rows).fill(null).map(_ => Array(columns).fill(0));
    
    const dfs = (r, c, preVal)=> {
      if (r < 0 || r == rows || c < 0 || c == columns || grid[r][c] <= preVal) return 0
      if (dp[r][c]) return dp[r][c]
      return dp[r][c] = (1 + dfs(r + 1, c, grid[r][c]) + 
                         dfs(r - 1, c, grid[r][c]) + 
                         dfs(r , c + 1, grid[r][c]) +  
                         dfs(r , c - 1, grid[r][c])) % mod;
    }
     for(let i = 0; i < rows; i++) {
      for(let j = 0; j < columns; j++) {
        result += dfs(i, j, -1) % mod;
      }
    }
   
    return result % mod;
  };



// 34/36 testcase solution

/**
 * @param {number[][]} grid
 * @return {number}
 */
var countPaths = function(grid) {
    const mod = Math.pow(10, 9) + 7;
    const m = grid.length;
    const n = grid[0].length;
    const dp = Array(m)
      .fill(null)
      .map(() => Array(n).fill(0));
  
    const dfs = (i, j) => {
      if (dp[i][j] > 0) {
        return dp[i][j];
      }
      let count = 0;
      const direction = [
        [0, -1],
        [-1, 0],
        [0, 1],
        [1, 0],
      ];
      for (const [dx, dy] of direction) {
        const x = i + dx;
        const y = j + dy;
        if (x >= 0 && x < m && y >= 0 && y < n && grid[x][y] > grid[i][j]) {
          count = dfs(x, y)
        }
      }
      dp[i][j] = count;
      return count;
    };
  
    let paths = 0;
    for (let i = 0; i < m; i++) {
      for (let j = 0; j < n; j++) {
        dfs(i, j)
      }
    }
    for (let row = 0; row < m; row ++){
        paths += dp[row].reduce((total, val) =>{return total + val}, 0)
        paths /= mod
    }
    return paths;
  };