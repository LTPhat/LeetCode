# You are given an integer n. We reorder the digits in any order (including the original order) such that the leading digit is not zero.

# Return true if and only if we can do this so that the resulting number is a power of two.

 

# Example 1:

# Input: n = 1
# Output: true
# Example 2:

# Input: n = 10
# Output: false
 

# Constraints:

# 1 <= n <= 109

class Solution(object):
    def reorderedPowerOf2(self, n):
        """
        :type n: int
        :rtype: bool
        """
        power_set = set()
        k = 0
        i = 0
        while k <= 10**9:
            k = 2**i
            number_str = "".join(sorted(str(k)))
            power_set.add(number_str)
            i += 1
        return "".join(sorted(str(n))) in power_set