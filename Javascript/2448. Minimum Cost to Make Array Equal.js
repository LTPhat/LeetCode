// You are given two 0-indexed arrays nums and cost consisting each of n positive integers.

// You can do the following operation any number of times:

// Increase or decrease any element of the array nums by 1.
// The cost of doing one operation on the ith element is cost[i].

// Return the minimum total cost such that all the elements of the array nums become equal.

 

// Example 1:

// Input: nums = [1,3,5,2], cost = [2,3,1,14]
// Output: 8
// Explanation: We can make all the elements equal to 2 in the following way:
// - Increase the 0th element one time. The cost is 2.
// - Decrease the 1st element one time. The cost is 3.
// - Decrease the 2nd element three times. The cost is 1 + 1 + 1 = 3.
// The total cost is 2 + 3 + 3 = 8.
// It can be shown that we cannot make the array equal with a smaller cost.
// Example 2:

// Input: nums = [2,2,2,2,2], cost = [4,2,8,1,3]
// Output: 0
// Explanation: All the elements are already equal, so no operations are needed.
 

// Constraints:

// n == nums.length == cost.length
// 1 <= n <= 105
// 1 <= nums[i], cost[i] <= 106

// Binary Search Approach:
// Algorithm
// Initialize the searching space by setting its boundaries left = min(nums) and right = max(nums).
// 2）While left < right:

// Get the middle value mid using integer division mid = (left + right) / 2.
// Calculate the cost of two adjacent bases, F(mid) and F(mid + 1).
// If F(x)<F(x+1)F(x) < F(x + 1)F(x)<F(x+1), it means the base that brings the minimum cost is on F(x)F(x)F(x)'s left, thus we should cut the right half.
// If F(x)>=F(x+1)F(x) >= F(x + 1)F(x)>=F(x+1), it means the base that brings the minimum cost is on F(x)F(x)F(x)'s right, thus we should cut the left half.
// If F(mid) > F(mid + 1), cut the left half by setting left = mid + 1. Otherwise, cut the right half by setting right = mid. Then repeat step 2.
// Return left once the search ends.


/**
 * @param {number[]} nums
 * @param {number[]} cost
 * @return {number}
 */
var minCost = function(nums, cost) {
    function findCost(base){
        let totalCost = 0
        for (let [index, value] of nums.entries()){
            totalCost += Math.abs(value - base) * cost[index]
            }
            return totalCost
        }
    let low = Math.min(...nums)
    let high = Math.max(...nums)
    while (low < high){
        let mid = Math.floor((low + high)/2)
        console.log(mid)
        if (findCost(mid) < findCost(mid + 1)){
            high = mid
        }else{
            low = mid + 1
        }
    }
    return findCost(low)
};