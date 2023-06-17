// Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

// Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

// Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

// Return the minimum integer k such that she can eat all the bananas within h hours.

 

// Example 1:

// Input: piles = [3,6,7,11], h = 8
// Output: 4
// Example 2:

// Input: piles = [30,11,23,4,20], h = 5
// Output: 30
// Example 3:

// Input: piles = [30,11,23,4,20], h = 6
// Output: 23


#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

int minEatingSpeed(vector<int>& piles, int h) {
    auto getEatingHours = [](const vector<int>& piles, int speed) {
        int totalHours = 0;
        for (int pile : piles) {
            totalHours += ceil(static_cast<double>(pile) / speed);
        }
        return totalHours;
    };

    int lowSpeed = 1;
    int highSpeed = *max_element(piles.begin(), piles.end());
    while (lowSpeed <= highSpeed) {
        int mid = ceil(static_cast<double>(lowSpeed + highSpeed) / 2);
        if (getEatingHours(piles, mid) <= h) {
            highSpeed = mid - 1;
        } else {
            lowSpeed = mid + 1;
        }
    }

    return lowSpeed;
}