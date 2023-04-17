# You have n dice, and each die has k faces numbered from 1 to k.

# Given three integers n, k, and target, return the number of possible ways (out of the kn total ways) to roll the dice, so the sum of the face-up numbers equals target. Since the answer may be too large, return it modulo 109 + 7.

 

# Example 1:

# Input: n = 1, k = 6, target = 3
# Output: 1
# Explanation: You throw one die with 6 faces.
# There is only one way to get a sum of 3.
# Example 2:

# Input: n = 2, k = 6, target = 7
# Output: 6
# Explanation: You throw two dice, each with 6 faces.
# There are 6 ways to get a sum of 7: 1+6, 2+5, 3+4, 4+3, 5+2, 6+1.
# Example 3:

# Input: n = 30, k = 30, target = 500
# Output: 222616187
# Explanation: The answer must be returned modulo 10**9 + 7.
 

# Constraints:

# 1 <= n, k <= 30
# 1 <= target <= 1000


#Algorithm: DYNAMIC PROGRAMING

# As an initial example, pretend we have 5 dice with 6 faces each and we want to determine how many ways to make 18.
# In other words, what is dp(5, 6, 18)?

# At first glance, this is seems difficult and overwhelming. But if we make one simple observation, we can reduce this big problem into several smaller sub-problems. We have 5 dice, but let's first just look at ONE of these dice (say the last one). This die can take on f=6 different values (1 to 6), so we consider what happens when we fix its value to each possibility (6 cases):

# Case 1: The last die is a 1. The remaining 4 dice must sum to 18-1=17. This can happen dp(4, 6, 17) ways.
# Case 2: The last die is a 2. The remaining 4 dice must sum to 18-2=16. This can happen dp(4, 6, 16) ways.
# Case 3: The last die is a 3. The remaining 4 dice must sum to 18-3=15. This can happen dp(4, 6, 15) ways.
# Case 4: The last die is a 4. The remaining 4 dice must sum to 18-4=14. This can happen dp(4, 6, 14) ways.
# Case 5: The last die is a 5. The remaining 4 dice must sum to 18-5=13. This can happen dp(4, 6, 13) ways.
# Case 6: The last die is a 6. The remaining 4 dice must sum to 18-6=12. This can happen dp(4, 6, 12) ways.

# dp(5, 6, 18) = dp(4, 6, 17) + dp(4, 6, 16) + dp(4, 6, 15) + dp(4, 6, 14) + dp(4, 6, 13) + dp(4, 6, 12)

# The DP formula
#//////////////////////////////////
# dp(d, f, target) = dp(d-1, f, target-1) + dp(d-1, f, target-2) + ... + dp(d-1, f, target-f)
#//////////////////////////////////

# The base case occurs when d = 0. We can make target=0 with 0 dice, but nothing else.
# So dp(0, f, t) = 0 if t != 0, and dp(0, f, 0) = 1.

#Create a memorization dict to avoid recalculating and TLE

class Solution(object):
    def numRollsToTarget(self, n, k, target):
        """
        :type n: int
        :type k: int
        :type target: int
        :rtype: int
        """
        MOD = 10**9 + 7
        memo = {} # Save dp to avoid TLE
        def dp(dice, target): 
            #Base case
            if dice == 0:
                if target == 0:
                    return 1
                else:
                    return 0
            if (dice, target) in memo:
                return memo[(dice, target)]
            count = 0
            for face in range (1, k+1):
                count += dp(dice-1, target-face) 
            memo[(dice, target)] = count
            return count
        return dp(n,target) % MOD

