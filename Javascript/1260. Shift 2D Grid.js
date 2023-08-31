// Given a 2D grid of size m x n and an integer k. You need to shift the grid k times.

// In one shift operation:

// Element at grid[i][j] moves to grid[i][j + 1].
// Element at grid[i][n - 1] moves to grid[i + 1][0].
// Element at grid[m - 1][n - 1] moves to grid[0][0].
// Return the 2D grid after applying shift operation k times.

 

// Example 1:


// Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1
// Output: [[9,1,2],[3,4,5],[6,7,8]]
// Example 2:


// Input: grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4
// Output: [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]
// Example 3:

// Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 9
// Output: [[1,2,3],[4,5,6],[7,8,9]]

/**
 * @param {number[][]} grid
 * @param {number} k
 * @return {number[][]}
 */
var shiftGrid = function(grid, k) {
    function get_last_column(grid){
        let lastColumn = [];
        for (let i = 0; i < grid.length; i++) {
        lastColumn.push(grid[i][grid[i].length - 1]);
        }
        return lastColumn
    }
    let m = grid.length
    let n = grid[0].length
    for (let time = 0; time < k; time++){
        last_column = get_last_column(grid)
        for (let j = n - 1; j > 0; j--){
            for(let i = 0; i < m ; i++){
                grid[i][j] = grid[i][j-1]
            }
        }
        ll = last_column.length
        grid[0][0] = last_column[ll-1]
        for (let i = 1; i < m ; i++){
            grid[i][0] = last_column[i - 1]
        }
    }
    return grid
};