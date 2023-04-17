// Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

// Return the array in the form [x1,y1,x2,y2,...,xn,yn].

 

// Example 1:

// Input: nums = [2,5,1,3,4,7], n = 3
// Output: [2,3,5,4,1,7] 
// Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].
// Example 2:

// Input: nums = [1,2,3,4,4,3,2,1], n = 4
// Output: [1,4,2,3,3,2,4,1]
// Example 3:

// Input: nums = [1,1,2,2], n = 2
// Output: [1,2,1,2]



// C1: Using slice method

/**
 * @param {number[]} nums
 * @param {number} n
 * @return {number[]}
 */
var shuffle = function(nums, n) {
    let second = nums.slice(n);
    nums = nums.slice(0,n);
    for (let i = 0; i < second.length; i++){
        nums.splice(2*i + 1, 0, second[i]);
    }
    return nums;
};


// C2: For loop
var shuffle = function(nums, n) {
    let result = [];
    for(let i = 0; i < n; i++){
        result.push(nums[i]);
        result.push(nums[i+n]);   
    }
    return result;
};