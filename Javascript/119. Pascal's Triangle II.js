// Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

// In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

// Example 1:

// Input: rowIndex = 3
// Output: [1,3,3,1]
// Example 2:

// Input: rowIndex = 0
// Output: [1]
// Example 3:

// Input: rowIndex = 1
// Output: [1,1]


/**
 * @param {number} rowIndex
 * @return {number[]}
 */
var getRow = function(rowIndex) {
    const tri = [[1], []];
        for (let i = 1; i <= rowIndex; i++) {
            const currRow = tri[1];
            const prevRow = tri[0];
            for (let e = 0; e <= i; e++) {
                if (e === 0 || e === i) {
                    currRow.push(1);
                } else {
                    currRow.push(prevRow[e - 1] + prevRow[e]);
                }
            }
            tri[0] = currRow.slice();
            tri[1] = [];
        }
        return tri[0];

};