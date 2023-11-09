// You are given an n x n binary matrix grid where 1 represents land and 0 represents water.

// An island is a 4-directionally connected group of 1's not connected to any other 1's. There are exactly two islands in grid.

// You may change 0's to 1's to connect the two islands to form one island.

// Return the smallest number of 0's you must flip to connect the two islands.

 

// Example 1:

// Input: grid = [[0,1],[1,0]]
// Output: 1
// Example 2:

// Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
// Output: 2
// Example 3:

// Input: grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
// Output: 1
 

// Constraints:

// n == grid.length == grid[i].length
// 2 <= n <= 100
// grid[i][j] is either 0 or 1.
// There are exactly two islands in grid.

// DFS to get all 1's of one island into deque first
// Increase res by 1 after iterating all element in deque given the condition that deque is not empty
// Return res if find another 1's cell while doing BFS


/**
 * @param {number[][]} grid
 * @return {number}
 */
var shortestBridge = function(grid) {
    const N = grid.length
    let visit = new Set()
    let deque = []
    const direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    function invalid(row, col){
        return row < 0 || col < 0 || row === N || col === N
    }


    function dfs(row, col){
        if (invalid(row, col) || visit.has(`${row},${col}`) || grid[row][col] == 0){
            return 
        }
        visit.add(`${row},${col}`)
        deque.push([row, col])
        for (let dx of direction){
            dfs(row + dx[0], col + dx[1])
        }
    }

    function bfs(){
        let res = 0
        while (deque.length != 0){
            let n = deque.length
            for (let i = 0; i < n; i++){
                let [r, c]= deque.shift()
                for (let [dr, dc] of direction){
                    currRow = r + dr
                    currCol = c + dc
                    if (invalid(currRow, currCol) || visit.has(`${currRow},${currCol}`)){
                        continue
                    }
                    if (grid[currRow][currCol]){
                        return res
                    }
                    deque.push([currRow, currCol])
                    visit.add(`${currRow},${currCol}`)
                }
            }
            res += 1
        }
    }

    for (let i = 0; i < N; i++){
        for (let j = 0; j < N; j++){
            if (grid[i][j] === 1){
                dfs(i, j)
                return bfs()
            }
        }
    }
};