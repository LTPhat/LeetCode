// Given a 0-indexed integer array nums, find a 0-indexed integer array answer where:

// answer.length == nums.length.
// answer[i] = |leftSum[i] - rightSum[i]|.
// Where:

// leftSum[i] is the sum of elements to the left of the index i in the array nums. If there is no such element, leftSum[i] = 0.
// rightSum[i] is the sum of elements to the right of the index i in the array nums. If there is no such element, rightSum[i] = 0.
// Return the array answer.

 

// Example 1:

// Input: nums = [10,4,8,3]
// Output: [15,1,11,22]
// Explanation: The array leftSum is [0,10,14,22] and the array rightSum is [15,11,3,0].
// The array answer is [|0 - 15|,|10 - 11|,|14 - 3|,|22 - 0|] = [15,1,11,22].
// Example 2:

// Input: nums = [1]
// Output: [0]
// Explanation: The array leftSum is [0] and the array rightSum is [0].
// The array answer is [|0 - 0|] = [0].


#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
    int sum(vector<int> nums, int index){
        int sum = 0;
        for (int i = 0; i < index; i++){
            sum += nums[i];
        }
        return sum;
    }
    int leftSum(vector<int> nums, int index){
            if (index == 0){
                return 0;
            }
            return sum(nums, index);
        }
    int rightSum(vector<int> nums, int index){
            if (index == nums.size() - 1){
                return 0;
            }
            return sum(nums, nums.size()) - leftSum(nums, index) - nums[index];
        }
    vector<int> leftRigthDifference(vector<int>& nums) {
        vector<int> answer(nums.size());
        for (int i = 0; i < nums.size(); i++){
            answer[i] = abs(leftSum(nums, i)-rightSum(nums, i));
        }
        return answer;
    }
};