# You are given an integer n.

# Each number from 1 to n is grouped according to the sum of its digits.

# Return the number of groups that have the largest size.

 

# Example 1:

# Input: n = 13
# Output: 4
# Explanation: There are 9 groups in total, they are grouped according sum of its digits of numbers from 1 to 13:
# [1,10], [2,11], [3,12], [4,13], [5], [6], [7], [8], [9].
# There are 4 groups with largest size.
# Example 2:

# Input: n = 2
# Output: 2
# Explanation: There are 2 groups [1], [2] of size 1.
 

# Constraints:

# 1 <= n <= 104
from collections import defaultdict

class Solution(object):
    def count_sum_digit(self, num):
            """
            Calculate sum of digit of a number
            """
            ans = 0
            while num > 0:
                ans += num % 10
                num = num // 10
            return ans
    def countLargestGroup(self, n):
        """
        :type n: int
        :rtype: int
        """
        store_map = defaultdict(int)
        max_value = 0
        for i in range(1, n + 1):
            curr_sum = self.count_sum_digit(i)
            store_map[curr_sum] += 1
            max_value = max(max_value, store_map[curr_sum])

        return sum(1 for val in store_map.values() if val == max_value)
        
        