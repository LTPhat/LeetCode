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

class Solution {
public:
    string convertToTitle(int columnNumber) {
         if (columnNumber < 27) {
        return std::string(1, 'A' + (columnNumber - 1));
    }
    
    std::string ans = "";
    while (columnNumber > 0) {
        int charValue = columnNumber % 26;
        if (charValue == 0) {
            ans += std::string(1, 'Z');
            columnNumber = (columnNumber / 26) - 1;
        } else {
            ans += std::string(1, 'A' + (charValue - 1));
            columnNumber /= 26;
        }
    }
    
    std::reverse(ans.begin(), ans.end());
    return ans;
    }
};