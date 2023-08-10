// You are given a 0-indexed integer array nums and an integer p. Find p pairs of indices of nums such that the maximum difference amongst all the pairs is minimized. Also, ensure no index appears more than once amongst the p pairs.

// Note that for a pair of elements at the index i and j, the difference of this pair is |nums[i] - nums[j]|, where |x| represents the absolute value of x.

// Return the minimum maximum difference among all p pairs. We define the maximum of an empty set to be zero.

 

// Example 1:

// Input: nums = [10,1,2,7,1,3], p = 2
// Output: 1
// Explanation: The first pair is formed from the indices 1 and 4, and the second pair is formed from the indices 2 and 5. 
// The maximum difference is max(|nums[1] - nums[4]|, |nums[2] - nums[5]|) = max(0, 1) = 1. Therefore, we return 1.
// Example 2:

// Input: nums = [4,2,1,2], p = 1
// Output: 0
// Explanation: Let the indices 1 and 3 form a pair. The difference of that pair is |2 - 2| = 0, which is the minimum we can attain.

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool checkPPair(const vector<int>& nums, int value, int p) {
    int count = 0;
    int i = 0;
    while (i < nums.size()) {
        if (abs(nums[i] - nums[i + 1]) <= value) {
            count += 1;
            i += 2;
        } else {
            i += 1;
        }
        if (count == p) {
            return true;
        }
    }
    return false;
}

int minimizeMax(vector<int>& nums, int p) {
    if (p == 0) return 0;
    
    sort(nums.begin(), nums.end());
    int left = 0;
    int n = nums.size();
    int right = nums[n - 1] - nums[0];
    
    while (left <= right) {
        int mid_val = (left + right) / 2;
        if (checkPPair(nums, mid_val, p)) {
            right = mid_val - 1;
        } else {
            left = mid_val + 1;
        }
    }
    return left;
}
