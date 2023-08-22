// Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

// For example:

// A -> 1
// B -> 2
// C -> 3
// ...
// Z -> 26
// AA -> 27
// AB -> 28 
// ...
 

// Example 1:

// Input: columnNumber = 1
// Output: "A"
// Example 2:

// Input: columnNumber = 28
// Output: "AB"
// Example 3:

// Input: columnNumber = 701
// Output: "ZY"
 

// Constraints:

// 1 <= columnNumber <= 231 - 1


/**
 * @param {number} columnNumber
 * @return {string}
 */
var convertToTitle = function(columnNumber) {
    if (columnNumber < 27){
        return String.fromCharCode("A".charCodeAt(0) + (columnNumber - 1))
    }
    let ans = ""
    while (columnNumber > 0){
        char = columnNumber % 26
        if (char === 0){
            ans += "Z".repeat(1)
            columnNumber = parseInt(columnNumber / 26) - 1
        }else{
            ans += String.fromCharCode("A".charCodeAt(0) + (char - 1))
            columnNumber = parseInt(columnNumber / 26)
        }
    }
    return ans.split("").reverse().join("")
};