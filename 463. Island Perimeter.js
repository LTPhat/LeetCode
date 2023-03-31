// You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

// Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

// The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

 

// Example 1:


// Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
// Output: 16
// Explanation: The perimeter is the 16 yellow stripes in the image above.
// Example 2:

// Input: grid = [[1]]
// Output: 4
// Example 3:

// Input: grid = [[1,0]]
// Output: 4
 

// Constraints:

// row == grid.length
// col == grid[i].length
// 1 <= row, col <= 100
// grid[i][j] is 0 or 1.
// There is exactly one island in grid.



// Approach 1: DFS

// Base case: 
// If the cell A just outside boundary: perimeter += 1
// If the neighbor cell of the A is water: perimeter += 1
// If the cell A is visited: continue

/**
 * @param {number[][]} grid
 * @return {number}
 */
var islandPerimeter = function(grid) {
    const visited = [];
    function dfs(row, col){
        // Base case
        if (row < 0 || row >= grid.length || col < 0 || col >= grid[0].length || grid[row][col] == 0) return 1;
        if (grid[row][col] == -1) return 0; // check if the cell is visited
        grid[row][col] = -1; // Set visited 
        const direction = [[-1, 0], [0, 1], [1, 0], [0, -1]];
        let perimeter = 0;
        for (let go of direction){
            perimeter += dfs(row + go[0], col + go[1]);
        }
        return perimeter;
    }
    for (let i = 0; i < grid.length; i++){
        for (let j = 0; j < grid[0].length; j++){
            if (grid[i][j] == 1){
                return dfs(i, j);
            }
        }
    }
    return 0;
};


// Approach 2: Math ---> Add 4 for each land and remove 2 for each internal common edge

var islandPerimeter = function(grid) {
    if (grid == null || grid.length == 0 || grid[0].length == 0) return 0;
    let result = 0;
    for (let i = 0; i < grid.length; i++) {
        for (let j = 0; j < grid[0].length; j++) {
            if (grid[i][j] == 1) {
                result += 4;
                if (i > 0 && grid[i-1][j] == 1) result -= 2;
                if (j > 0 && grid[i][j-1] == 1) result -= 2;
            }
        }
    }
    return result;
};