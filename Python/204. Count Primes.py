# // Given an integer n, return the number of prime numbers that are strictly less than n.

 

# // Example 1:

# // Input: n = 10
# // Output: 4
# // Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
# // Example 2:

# // Input: n = 0
# // Output: 0
# // Example 3:

# // Input: n = 1
# // Output: 0
 

# // Constraints:

# // 0 <= n <= 5 * 106


# Slave of Eratosthenes

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1 or n == 0:
            return 0
        check = [True for i in range(0, n)]
        p = 2
        while (p ** 2 <= n):
            if check[p]:
                for i in range(p * p, n, p):
                    check[i] = False
            p += 1
        return check.count(True) - 2
        