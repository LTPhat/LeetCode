// Given an n x n grid containing only values 0 and 1, where 0 represents water and 1 represents land, find a water cell such that its distance to the nearest land cell is maximized, and return the distance. If no land or water exists in the grid, return -1.

// The distance used in this problem is the Manhattan distance: the distance between two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.

 

// Example 1:


// Input: grid = [[1,0,1],[0,0,0],[1,0,1]]
// Output: 2
// Explanation: The cell (1, 1) is as far as possible from all the land with distance 2.
// Example 2:


// Input: grid = [[1,0,0],[0,0,0],[0,0,0]]
// Output: 4
// Explanation: The cell (2, 2) is as far as possible from all the land with distance 4.
 

// Constraints:

// n == grid.length
// n == grid[i].length
// 1 <= n <= 100
// grid[i][j] is 0 or 1


// Algorithm : Breadth-First Search

// First, Set a queue to store all the (x,y) of land cell (which has value 1)
// While deque is not empty{
    // Get the front cell (u)
    //find all neighbor water cell (which has value 0) (Zi)and add to deque, increase the value of water cell by one to mark the distance from u to Zi
//} 




/**
 * @param {number[][]} grid
 * @return {number}
 */
var maxDistance = function(grid) {
    let n = grid.length;
    let deque = new Array();
    let direction = [[0, 1], [-1, 0], [0, -1], [1,0]];
    // Push all the land cell into deque first.
    for (let i = 0; i < n; i++){
        for (let j = 0; j < n; j++){
            if (grid[i][j] == 1){
                deque.push([i, j]);
            }
        }
    }
    let res = -1; 
    while(deque.length != 0){
        // Take left-most element
        let front = deque.shift();
        let r = front[0];
        let c = front[1];
        res = grid[r][c];
        // Find around that cell
        for (let dir of direction){
            let newR = r + dir[0];
            let newC = c + dir[1];
            // Check boundary and find water cell
            if((Math.min(newR, newC) >=0) && (Math.max(newR, newC) < n)
            && (grid[newR][newC] == 0)){
                deque.push([newR, newC]);
                grid[newR][newC] = grid[r][c] + 1;
            }
        }
    }
    return res > 1 ? res - 1: -1;
};