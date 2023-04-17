# For an integer array nums, an inverse pair is a pair of integers [i, j] where 0 <= i < j < nums.length and nums[i] > nums[j].

# Given two integers n and k, return the number of different arrays consist of numbers from 1 to n such that there are exactly k inverse pairs. Since the answer can be huge, return it modulo 109 + 7.

 

# Example 1:

# Input: n = 3, k = 0
# Output: 1
# Explanation: Only the array [1,2,3] which consists of numbers from 1 to 3 has exactly 0 inverse pairs.
# Example 2:

# Input: n = 3, k = 1
# Output: 2
# Explanation: The array [1,3,2] and [2,1,3] have exactly 1 inverse pair.
 

# Constraints:

# 1 <= n <= 1000
# 0 <= k <= 1000

#Algorithm

# Call function f(n,k) is the number of case 
# Take an example: n = 3, k = 2, so we have array a consist of {1,2,3}
# So now, we have to calculate f(3,2)
#   - In case [, ,3] --> There is no reverve pair consist {3} because {3} is the largest digit and it's is at the largest index
# ---> The case remain is f(2,2) = 0 because array with 2 elements can not create 2 reverse pair
#   - In case [,3,] --> There is 1 reverse pair {3,a[2]}
# ---> The case remain is f(2,1) = 1 which is [2,3,1]
#   - In case [3, ,] --> There are 2 reverse pairs {3,a[1]}, {3,a[2]}
# ---> The case reamin is f(2,0) = 1 which is [3,1,2]

# So f(3,2) = f(2,2) + f(2,1) + f(2,0)

#DP equation: f(n,k) = f(n-1,k) + f(n-1,k-1) + f(n-1,k-2) + ... + f(n-1,k-(n-1)) (1)

#             f(n,k-1) = f(n-1,k-1) + f(n-1,k-2) + ... + f(n-1,n-k)  (2)

# (1) - (2): f(n,k) - f(n,k-1) = f(n-1,k) - f(n-1,n-k)

#           => f(n,k) = f(n,k-1) + f(n-1,k) - f(n-1,n-k) (DP equation in coding)

# Base case: 
#   k < 0 or n <= 0  --> No cases
#   n = 1 and k >= 1 --> No cases
#   k = 0, n > 0 --> 1 case

class Solution(object):
    def kInversePairs(self, n, k):
        dp={}
        def record_dp(n,k):
            if (n,k) in dp:
                return dp[(n,k)]
            if k == 0 and n > 0:
                return 1
            if k < 0  or n <= 0:
                return 0
            if n == 1 and k >= 1:
                return 0
            dp[(n,k)] = (record_dp(n-1,k) + record_dp(n,k-1) - record_dp(n-1,k-n))%(10**9+7)
            return dp[(n,k)] 
        return record_dp(n,k)