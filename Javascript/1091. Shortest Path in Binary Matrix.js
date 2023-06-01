// Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

// A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

// All the visited cells of the path are 0.
// All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
// The length of a clear path is the number of visited cells of this path.

 

// Example 1:


// Input: grid = [[0,1],[1,0]]
// Output: 2
// Example 2:


// Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
// Output: 4
// Example 3:

// Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
// Output: -1


/**
 * @param {number[][]} grid
 * @return {number}
 */
var shortestPathBinaryMatrix = function(grid) {
    function invalid(row, col, n){
        return row < 0 || col < 0 || row === n || col === n
    }
    const n = grid.length
    if (grid[0][0] || grid[n - 1][n - 1]) return -1
    const directions = [
		[1, 0],
		[-1, 0],
		[0, 1],
		[0, -1],
		[1, 1],
		[1, -1],
		[-1, 1],
		[-1, -1],
	];
    let deque = [[0, 0, 1]]
    while(deque.length){
        const [row, col, dis] = deque.shift()
        if (row == n - 1 && col == n - 1) return dis
        for (const [dx, dy] of directions){
            let x = row + dx
            let y = col + dy
            if (invalid(x, y, n) || grid[x][y] != 0) continue
            deque.push([x, y, dis + 1])
            grid[x][y] = 1
        }
    }
    return -1
};
