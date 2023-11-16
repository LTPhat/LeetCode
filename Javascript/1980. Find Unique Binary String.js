// Given an array of strings nums containing n unique binary strings each of length n, return a binary string of length n that does not appear in nums. If there are multiple answers, you may return any of them.

 

// Example 1:

// Input: nums = ["01","10"]
// Output: "11"
// Explanation: "11" does not appear in nums. "00" would also be correct.
// Example 2:

// Input: nums = ["00","01"]
// Output: "11"
// Explanation: "11" does not appear in nums. "10" would also be correct.
// Example 3:

// Input: nums = ["111","011","001"]
// Output: "101"
// Explanation: "101" does not appear in nums. "000", "010", "100", and "110" would also be correct.
/**
 * @param {string[]} nums
 * @return {string}
 */
var findDifferentBinaryString = function(nums) {
    const n = nums.length;

   for (let i = 0; i < Math.pow(2, n); i++) {
       let numStr = i.toString(2);

       while (numStr.length < n) {
           numStr = '0' + numStr;
       }

       if (!nums.includes(numStr)) {
           return numStr;
       }
   }
};