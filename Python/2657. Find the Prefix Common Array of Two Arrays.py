# You are given two 0-indexed integer permutations A and B of length n.

# A prefix common array of A and B is an array C such that C[i] is equal to the count of numbers that are present at or before the index i in both A and B.

# Return the prefix common array of A and B.

# A sequence of n integers is called a permutation if it contains all integers from 1 to n exactly once.

 

# Example 1:

# Input: A = [1,3,2,4], B = [3,1,2,4]
# Output: [0,2,3,4]
# Explanation: At i = 0: no number is common, so C[0] = 0.
# At i = 1: 1 and 3 are common in A and B, so C[1] = 2.
# At i = 2: 1, 2, and 3 are common in A and B, so C[2] = 3.
# At i = 3: 1, 2, 3, and 4 are common in A and B, so C[3] = 4.
# Example 2:

# Input: A = [2,3,1], B = [3,1,2]
# Output: [0,1,3]
# Explanation: At i = 0: no number is common, so C[0] = 0.
# At i = 1: only 3 is common in A and B, so C[1] = 1.
# At i = 2: 1, 2, and 3 are common in A and B, so C[2] = 3.
 

# Constraints:

# 1 <= A.length == B.length == n <= 50
# 1 <= A[i], B[i] <= n
# It is guaranteed that A and B are both a permutation of n integers.


class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        # # O(n^2) sol
        # fre_count = {}
        # length = len(A)
        # seen = set()
        # ans = [0] * length
        # for i in range(0, length): 
        #     fre_count[A[i]] = fre_count.get(A[i], 0) + 1
        #     fre_count[B[i]] = fre_count.get(B[i], 0) + 1
        #     for key in fre_count.keys():
        #         if fre_count[key] == 2:
        #             ans[i] += 1
        
        # return ans

        # O(n) sol

        n = len(A)
        result = [0] * n
        count = 0
        fre_count = [0] * (n + 1)
        
        for i in range(n):
            fre_count[A[i]] += 1
            if fre_count[A[i]] == 2:
                count += 1
            
            fre_count[B[i]] += 1
            if fre_count[B[i]] == 2:
                count += 1
            
            result[i] = count
        
        return result

