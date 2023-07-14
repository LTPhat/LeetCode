// // Given an integer array arr and an integer difference, return the length of the longest subsequence in arr which is an arithmetic sequence such that the difference between adjacent elements in the subsequence equals difference.

// // A subsequence is a sequence that can be derived from arr by deleting some or no elements without changing the order of the remaining elements.

 

// // Example 1:

// // Input: arr = [1,2,3,4], difference = 1
// // Output: 4
// // Explanation: The longest arithmetic subsequence is [1,2,3,4].
// // Example 2:

// // Input: arr = [1,3,5,7], difference = 1
// // Output: 1
// // Explanation: The longest arithmetic subsequence is any single element.
// // Example 3:

// // Input: arr = [1,5,7,8,5,3,4,2,1], difference = -2
// // Output: 4
// // Explanation: The longest arithmetic subsequence is [7,5,3,1].
 

// // Constraints:

// // 1 <= arr.length <= 105
// // -104 <= arr[i], difference <= 104

// The key idea of the DP approach is to use a hash map dp to store the maximum length of an arithmetic subsequence that ends with each element in arr. We initialize dp as empty. Then, for each element arr[i], we check if arr[i] - difference is already present in dp.

// If it is, let's say dp[arr[i] - difference] = before_a. It means there exists an arithmetic subsequence of length before_a that ends with arr[i] - difference. Since we can append arr[i] to this sequence, we update dp[arr[i]] to be dp[arr[i] - difference] + 1.

// Otherwise, we simply set dp[arr[i]] = 1, as an element on its own is technically an arithmetic subsequence.


/**
 * @param {number[]} arr
 * @param {number} difference
 * @return {number}
 */
var longestSubsequence = function(arr, difference) {
    let dp = {}
    let ans = 0
    for (let i = 0; i < arr.length; i++){
        if(arr[i] - difference in dp){
            dp[arr[i]] = dp[arr[i] - difference] + 1
        }else{
            dp[arr[i]] = 1
        }
        ans = Math.max(ans, dp[arr[i]])
    }
    return ans
};