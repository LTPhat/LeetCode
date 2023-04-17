// Given two binary strings a and b, return their sum as a binary string.

 

// Example 1:

// Input: a = "11", b = "1"
// Output: "100"
// Example 2:

// Input: a = "1010", b = "1011"
// Output: "10101"



/**
 * @param {string} a
 * @param {string} b
 * @return {string}
 */
var addBinary = function(a, b) {
    let arrA = a.split("").reverse();
    let arrB = b.split("").reverse();
    let ans = [];
    const length = arrA.length > arrB.length ? arrA.length: arrB.length;
    let idx = 0;
    let carry = 0;
    while (idx < length){
        const first_digit = arrA[idx] ? +arrA[idx]: 0;
        const second_digit = arrB[idx] ? +arrB[idx]: 0;
        let sum = carry + first_digit + second_digit;
        carry = Math.floor(sum / 2);
        ans.unshift(sum % 2);
        idx += 1;
    }
    if (carry > 0) ans.unshift(carry);
    return ans.join("");
};