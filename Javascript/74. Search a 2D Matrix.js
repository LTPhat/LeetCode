// You are given an m x n integer matrix matrix with the following two properties:

// Each row is sorted in non-decreasing order.
// The first integer of each row is greater than the last integer of the previous row.
// Given an integer target, return true if target is in matrix or false otherwise.

// You must write a solution in O(log(m * n)) time complexity.

 

// Example 1:


// Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
// Output: true
// Example 2:


// Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
// Output: false
 

// Constraints:

// m == matrix.length
// n == matrix[i].length
// 1 <= m, n <= 100
// -104 <= matrix[i][j], target <= 104


/**
 * @param {number[][]} matrix
 * @param {number} target
 * @return {boolean}
 */
var searchMatrix = function(matrix, target) {
    let m = matrix.length
    let n = matrix[0].length
    let left = 0
    let right = m * n - 1
    let midIndex
    let midEle
    while(left <= right){
        midIndex = Math.floor((left + right) / 2)
        midEle = matrix[Math.floor(midIndex / n)][midIndex % n]
        if (midEle === target){
            return true        
        }else if (midEle < target){
            left = midIndex + 1
        }else{
            right = midIndex -1
        }
    }
    return false
};