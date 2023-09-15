// Given an integer n, return the number of prime numbers that are strictly less than n.

 

// Example 1:

// Input: n = 10
// Output: 4
// Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
// Example 2:

// Input: n = 0
// Output: 0
// Example 3:

// Input: n = 1
// Output: 0
 

// Constraints:

// 0 <= n <= 5 * 106

/**
 * @param {number} n
 * @return {number}
 */
var countPrimes = function(n) {
    if (n == 0 || n == 1)
            return 0
    check = Array(n).fill(true)
    p = 2
    while (p ** 2 <= n){
        if (check[p]){
            for (let i = p * p; i < n; i = i + p){
                check[i] = false
            }
        }
        p += 1
    }
    return check.filter((x) => x == true).length - 2 
};