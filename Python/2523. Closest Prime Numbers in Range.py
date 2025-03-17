# Given two positive integers left and right, find the two integers num1 and num2 such that:

# left <= num1 < num2 <= right .
# Both num1 and num2 are prime numbers.
# num2 - num1 is the minimum amongst all other pairs satisfying the above conditions.
# Return the positive integer array ans = [num1, num2]. If there are multiple pairs satisfying these conditions, return the one with the smallest num1 value. If no such numbers exist, return [-1, -1].

 

# Example 1:

# Input: left = 10, right = 19
# Output: [11,13]
# Explanation: The prime numbers between 10 and 19 are 11, 13, 17, and 19.
# The closest gap between any pair is 2, which can be achieved by [11,13] or [17,19].
# Since 11 is smaller than 17, we return the first pair.
# Example 2:

# Input: left = 4, right = 6
# Output: [-1,-1]
# Explanation: There exists only one prime number in the given range, so the conditions cannot be satisfied.


class Solution(object):
    def closestPrimes(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        if left == right:
            return [-1, -1]
        primes = [True for i in range(0, right + 1)]
        primes[0], primes[1] = False, False
        p = 2
        while p * p <= right:
            if primes[p]:
                for i in range(p * p, right + 1, p):
                    primes[i] = False
            p += 1

        list_of_primes = [i for i in range(left, right + 1) if primes[i]]
        ans = [-1, -1]
        min_diff = float("inf")
        
        for i in range(len(list_of_primes) - 1):
            diff = list_of_primes[i + 1] - list_of_primes[i] 
            if diff < min_diff:
                min_diff = diff
                ans = [list_of_primes[i], list_of_primes[i + 1]]
            if min_diff == 2: 
                break
        return ans
