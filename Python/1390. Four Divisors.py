# Given an integer array nums, return the sum of divisors of the integers in that array that have exactly four divisors. If there is no such integer in the array, return 0.

 

# Example 1:

# Input: nums = [21,4,7]
# Output: 32
# Explanation: 
# 21 has 4 divisors: 1, 3, 7, 21
# 4 has 3 divisors: 1, 2, 4
# 7 has 2 divisors: 1, 7
# The answer is the sum of divisors of 21 only.
# Example 2:

# Input: nums = [21,21]
# Output: 64
# Example 3:

# Input: nums = [1,2,3,4,5]
# Output: 0
 

# Constraints:

# 1 <= nums.length <= 104
# 1 <= nums[i] <= 105


class Solution(object):
    def sumFourDivisors(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def find_divisor(num):
            count = 0
            div_sum = 0
            for i in range(1, int(sqrt(num)) + 1):
                if num % i == 0:
                    j = num // i
                    if i == j:
                        count += 1
                        div_sum += i
                    else:
                        count += 2
                        div_sum += i + j
            return count, div_sum

        total_sum = 0
        for num in nums:
            count_div, div_sum = find_divisor(num)
            if count_div == 4:
                total_sum += div_sum
        
        return total_sum