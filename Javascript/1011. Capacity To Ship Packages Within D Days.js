// // A conveyor belt has packages that must be shipped from one port to another within days days.

// // The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.

// // Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days.

 

// // Example 1:

// // Input: weights = [1,2,3,4,5,6,7,8,9,10], days = 5
// // Output: 15
// // Explanation: A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
// // 1st day: 1, 2, 3, 4, 5
// // 2nd day: 6, 7
// // 3rd day: 8
// // 4th day: 9
// // 5th day: 10

// // Note that the cargo must be shipped in the order given, so using a ship of capacity 14 and splitting the packages into parts like (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) is not allowed.
// // Example 2:

// // Input: weights = [3,2,2,4,1,4], days = 3
// // Output: 6
// // Explanation: A ship capacity of 6 is the minimum to ship all the packages in 3 days like this:
// // 1st day: 3, 2
// // 2nd day: 2, 4
// // 3rd day: 1, 4
// // Example 3:

// // Input: weights = [1,2,3,1,1], days = 4
// // Output: 3
// // Explanation:
// // 1st day: 1
// // 2nd day: 2
// // 3rd day: 3
// // 4th day: 1, 1


// Intuition of this Problem:

// The intuition behind this code is that we want to find the minimum capacity of the ship that can ship all the packages within days days. We can use binary search to efficiently search for this minimum capacity.

// To perform binary search, we need to define the search range [left, right]. The minimum capacity should be at least as large as the largest package, so we set left to be the maximum weight in weights. The maximum capacity should be the sum of weights, so we set right to be the sum of all weights in weights.

// For each mid value in the search range [left, right], we simulate the shipping process to see if it can be done within days days using a ship with capacity mid. We start with the first package and add packages to the ship until it is full. When the ship is full, we start a new day and continue adding packages until all packages are shipped. We count the number of days needed to ship all packages with the current mid value.

// If the number of days needed with the current mid value is greater than days, it means that the ship capacity is too small, and we need to increase the capacity. Therefore, we set left = mid + 1. Otherwise, we can try to reduce the capacity by setting right = mid.

// We repeat this process until left >= right, at which point left is the minimum capacity of the ship that can ship all the packages within days days. We return left as the answer.

/**
 * @param {number[]} weights
 * @param {number} days
 * @return {number}
 */
var shipWithinDays = function(weights, days) {
    let high = weights.reduce((sum, element) => {return sum + element}, 0);
    let low = Math.max(...weights);
    while(low < high){
        let curr_days = 0;
        let mid = Math.floor((low + high) / 2);
        let curr_weights = 0;
        for (let weight of weights){
            if(curr_weights + weight > mid){
                curr_days += 1;
                curr_weights = 0;
            }
            curr_weights += weight;
        }
        if (curr_days < days){ // The weight capacity is too large
            high = mid;
        }else{
            low = mid + 1;  // The weight capacity is too small
        }
    }
    return low;
};

