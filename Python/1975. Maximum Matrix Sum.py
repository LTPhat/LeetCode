# You are given an n x n integer matrix. You can do the following operation any number of times:

# Choose any two adjacent elements of matrix and multiply each of them by -1.
# Two elements are considered adjacent if and only if they share a border.

# Your goal is to maximize the summation of the matrix's elements. Return the maximum sum of the matrix's elements using the operation mentioned above.

 

# Example 1:


# Input: matrix = [[1,-1],[-1,1]]
# Output: 4
# Explanation: We can follow the following steps to reach sum equals 4:
# - Multiply the 2 elements in the first row by -1.
# - Multiply the 2 elements in the first column by -1.
# Example 2:


# Input: matrix = [[1,2,3],[-1,-2,-3],[1,2,3]]
# Output: 16
# Explanation: We can follow the following step to reach sum equals 16:
# - Multiply the 2 last elements in the second row by -1.
 

class Solution(object):
    def maxMatrixSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        total_sum = 0
        min_abs_val = float("inf")
        count_neg = 0
        n = len(matrix)
        for i in range(n):
            for j in range(n):
                if abs(matrix[i][j]) < min_abs_val:
                    min_abs_val = abs(matrix[i][j])
                if matrix[i][j] < 0:
                    count_neg += 1
                total_sum += abs(matrix[i][j])
        
        if count_neg % 2 == 0:
            return total_sum

        return total_sum - 2 * min_abs_val
        
