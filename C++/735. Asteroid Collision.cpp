// We are given an array asteroids of integers representing asteroids in a row.

// For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

// Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

 

// Example 1:

// Input: asteroids = [5,10,-5]
// Output: [5,10]
// Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
// Example 2:

// Input: asteroids = [8,-8]
// Output: []
// Explanation: The 8 and -8 collide exploding each other.
// Example 3:

// Input: asteroids = [10,2,-5]
// Output: [10]
// Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.

#include <vector>
#include <cmath>
#include <stack>

std::vector<int> asteroidCollision(std::vector<int>& asteroids) {
    std::stack<int> stack;
    for (int item : asteroids) {
        if (stack.empty() || item > 0) {
            stack.push(item); // Push only positive item
        } else {
            while (!stack.empty() && stack.top() > 0 && std::abs(item) > stack.top()) {
                stack.pop();
            }
            if (!stack.empty() && stack.top() == std::abs(item)) {
                stack.pop(); // Two items are equal ==> Both explode
            } else {
                if (stack.empty() || stack.top() < 0) {
                    stack.push(item); // Negative item
                }
            }
        }
    }
    std::vector<int> result(stack.size());
    int i = stack.size() - 1;
    while (!stack.empty()) {
        result[i--] = stack.top();
        stack.pop();
    }
    return result;
}