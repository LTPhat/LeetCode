// You are given two positive integer arrays spells and potions, of length n and m respectively, where spells[i] represents the strength of the ith spell and potions[j] represents the strength of the jth potion.

// You are also given an integer success. A spell and potion pair is considered successful if the product of their strengths is at least success.

// Return an integer array pairs of length n where pairs[i] is the number of potions that will form a successful pair with the ith spell.

 

// Example 1:

// Input: spells = [5,1,3], potions = [1,2,3,4,5], success = 7
// Output: [4,0,3]
// Explanation:
// - 0th spell: 5 * [1,2,3,4,5] = [5,10,15,20,25]. 4 pairs are successful.
// - 1st spell: 1 * [1,2,3,4,5] = [1,2,3,4,5]. 0 pairs are successful.
// - 2nd spell: 3 * [1,2,3,4,5] = [3,6,9,12,15]. 3 pairs are successful.
// Thus, [4,0,3] is returned.
// Example 2:

// Input: spells = [3,1,2], potions = [8,5,8], success = 16
// Output: [2,0,2]
// Explanation:
// - 0th spell: 3 * [8,5,8] = [24,15,24]. 2 pairs are successful.
// - 1st spell: 1 * [8,5,8] = [8,5,8]. 0 pairs are successful. 
// - 2nd spell: 2 * [8,5,8] = [16,10,16]. 2 pairs are successful. 
// Thus, [2,0,2] is returned.


// Approach: Sorting, Binary Search, Two pointer

// We start by initializing the output array pairs with all zeros, and sorting the potions array in ascending order.

// For each spell in spells, we perform a binary search on the potions array to find the number of potions that form a successful pair with the current spell. We maintain two pointers left and right that initially point to the first and last indices
// of the potions array, respectively.

// We repeat the binary search until the left and right pointers meet or cross each other. In each iteration, we compute the product of the current spell and the middle potion using long integer multiplication to avoid integer overflow. If the product is greater than or equal to the success threshold, we move the right pointer to the left of the middle index. Otherwise, we move the left pointer to the right of the middle index.

// Once the binary search is complete, we set the corresponding element of pairs to the number of potions that come after the left pointer in the sorted potions array, which are guaranteed to form a successful pair with the current spell.

// Finally, we return the pairs array as the result.

/**
 * @param {number[]} spells
 * @param {number[]} potions
 * @param {number} success
 * @return {number[]}
 */
var successfulPairs = function(spells, potions, success) {
    let pairs = new Array(spells.length).fill(0);
    potions.sort((x, y) => {return x - y});
    for (let i = 0; i < spells.length; i++){
        let left = 0;
        let right = potions.length - 1;
        while (left <= right){
            let mid = Math.floor((left + right) / 2);
            if (spells[i] * potions[mid] >= success){
                right = mid - 1;
            }else{
                left = mid + 1;
            }
        }
        pairs[i] = potions.length - left;
    }
    return pairs;
};


