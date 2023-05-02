// You are given an array of unique integers salary where salary[i] is the salary of the ith employee.

// Return the average salary of employees excluding the minimum and maximum salary. Answers within 10-5 of the actual answer will be accepted.

 

// Example 1:

// Input: salary = [4000,3000,1000,2000]
// Output: 2500.00000
// Explanation: Minimum salary and maximum salary are 1000 and 4000 respectively.
// Average salary excluding minimum and maximum salary is (2000+3000) / 2 = 2500
// Example 2:

// Input: salary = [1000,2000,3000]
// Output: 2000.00000
// Explanation: Minimum salary and maximum salary are 1000 and 3000 respectively.
// Average salary excluding minimum and maximum salary is (2000) / 1 = 2000

#include<iostream>
#include<algorithm>
#include<math.h>
#include<vector>


using namespace std;

class Solution {
public:
    double average(vector<int>& salary) {
        sort(salary.begin(), salary.end());
        double sum = 0;
        for (int i = 0; i < salary.size(); i++) {
            sum += salary[i];
        }
        return (sum - salary[0] - salary[salary.size() - 1]) / (salary.size() - 2);
    }
};