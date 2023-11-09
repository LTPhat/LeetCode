// Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

// You have the following three operations permitted on a word:

// Insert a character
// Delete a character
// Replace a character
 

// Example 1:

// Input: word1 = "horse", word2 = "ros"
// Output: 3
// Explanation: 
// horse -> rorse (replace 'h' with 'r')
// rorse -> rose (remove 'r')
// rose -> ros (remove 'e')

// Tabulation
//   h o r s e
// r           3
// o           2
// s           1
//   5 4 3 2 1 0 
//             

// The base case is when one of the strings is empty. In this case, the minimum number of operations required is equal to the length of the non-empty string.

// For the general case, we can use the following recurrence relation: if the current characters in the two strings match, the minimum number of operations required is the same as the minimum number of operations required to convert the first i-1 characters in the first string to the first j-1 characters in the second string. Otherwise, we can either insert a character, delete a character, or replace a character. We can take the minimum of these three options and add one to get the minimum number of operations required to convert the first i characters in the first string to the first j characters in the second string.

// Example 2:

// Input: word1 = "intention", word2 = "execution"
// Output: 5
// Explanation: 
// intention -> inention (remove 't')
// inention -> enention (replace 'i' with 'e')
// enention -> exention (replace 'n' with 'x')
// exention -> exection (replace 'n' with 'c')
// exection -> execution (insert 'u')
 

// Constraints:

// 0 <= word1.length, word2.length <= 500
// word1 and word2 consist of lowercase English letters.


/**
 * @param {string} word1
 * @param {string} word2
 * @return {number}
 */
var minDistance = function(word1, word2) {
    let dp = [];
    // Create dp matrix
    for (let i = 0; i <= word2.length; i++){
        dp[i] = [];
        for (let j = 0; j <= word1.length; j++){
            dp[i][j] = Number.MAX_SAFE_INTEGER;
        }
    }

    for (let i = 0; i <= word2.length; i++){
        dp[i][word1.length] = word2.length - i;
    }
    for (let j = 0; j <= word1.length; j++){
        dp[word2.length][j] = word1.length - j;
    }

    for (let i = word2.length - 1; i > -1; i--){
        for(let j = word1.length - 1; j > -1; j--){
            if(word1[j] === word2[i]){
                dp[i][j] = dp[i+1][j+1];
            }else{
                dp[i][j] = 1 + Math.min(dp[i][j+1], dp[i+1][j], dp[i+1][j+1]);
            }
        }
    }
    return dp[0][0];
};

