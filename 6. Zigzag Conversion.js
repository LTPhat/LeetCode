// The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

// P   A   H   N
// A P L S I I G
// Y   I   R
// And then read line by line: "PAHNAPLSIIGYIR"

// Write the code that will take a string and make this conversion given a number of rows:

// string convert(string s, int numRows);
 

// Example 1:

// Input: s = "PAYPALISHIRING", numRows = 3
// Output: "PAHNAPLSIIGYIR"
// Example 2:

// Input: s = "PAYPALISHIRING", numRows = 4
// Output: "PINALSIGYAHRPI"
// Explanation:
// P     I    N
// A   L S  I G
// Y A   H R
// P     I
// Example 3:

// Input: s = "A", numRows = 1
// Output: "A"
 

// Constraints:

// 1 <= s.length <= 1000
// s consists of English letters (lower-case and upper-case), ',' and '.'.
// 1 <= numRows <= 1000


// Explaintion:

// ex1:

// numRows = 3
//  0   1   2   3   4   5   6   7   8   9   10  11  12  13
//  P   A   Y   P   A   L   I   S   H   I   R   I   N   G

// 0         4         8        12
// P         A         H        N
// A    P    L    S    I    I   G
// L         I         R  
// 3         7         11

//row = 0 or numRows - 1: The distance = 4 = 3 + 1

// numRows = 4
//  0   1   2   3   4   5   6   7   8   9   10  11  12  13
//  P   A   Y   P   A   L   I   S   H   I   R   I   N   G

// 0     6    12
// P     I    N
// A   L S  I G
// Y A   H R
// P     I
// 3     9

// row = 0 or numRows - 1: The distance = 6 = 4 + 2

// The distance of two consecutive letters in the same row is always  <= numRows +  number of intersect rows

// Case 1: row = 0 or numRows - 1 => The distance = numRows + (rows between) = numRows +  number of intersect rows

// Case 2: rows between top and bottom.

// Traverse with step = numRows +  number of intersect rows

// Calcate dist = 2 * (numRows - row) - 2 to grab all the letters in the same row between range (j,j+numRows +  number of intersect rows) each iteration

//  *           
//  *       * ==> dist = 2 * (numRows - row) - 1 -1 
//  *   *
//  *
// 

/**
 * @param {string} s
 * @param {number} numRows
 * @return {string}
 */
var convert = function(s, numRows) {
    let res = "";
    if (numRows==1){
        return s;
    }
    let inter = numRows - 2;
    for (let row = 0; row < numRows; row++){
        // The first and the last row
        if(row == 0 || row == numRows - 1){
            for (let i = row; i < s.length ; i += (numRows + inter)){
                res += s[i];
            }
        }else{ // Row in intersection region
            for (let j = row; j < s.length; j += (numRows + inter)){
                let dist = 2 * (numRows - row) - 2;
                if (j + dist < s.length){
                    res += s[j] + s[j+dist];
                }else{
                    res += s[j];
                }
            }
        }
    }
    return res;
};