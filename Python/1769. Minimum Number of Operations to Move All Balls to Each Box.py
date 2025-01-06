# You have n boxes. You are given a binary string boxes of length n, where boxes[i] is '0' if the ith box is empty, and '1' if it contains one ball.

# In one operation, you can move one ball from a box to an adjacent box. Box i is adjacent to box j if abs(i - j) == 1. Note that after doing so, there may be more than one ball in some boxes.

# Return an array answer of size n, where answer[i] is the minimum number of operations needed to move all the balls to the ith box.

# Each answer[i] is calculated considering the initial state of the boxes.

 

# Example 1:

# Input: boxes = "110"
# Output: [1,1,3]
# Explanation: The answer for each box is as follows:
# 1) First box: you will have to move one ball from the second box to the first box in one operation.
# 2) Second box: you will have to move one ball from the first box to the second box in one operation.
# 3) Third box: you will have to move one ball from the first box to the third box in two operations, and move one ball from the second box to the third box in one operation.
# Example 2:

# Input: boxes = "001011"
# Output: [11,8,5,4,3,4]
class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
        # Solution 1: Brute Force
        # ans = [0] * len(boxes) 
        # for i in range(0, len(boxes)):
        #     for j in range(0, len(boxes)):
        #         if j == i: 
        #             continue
        #         if boxes[j] == "1":
        #             ans[i] += abs(j - i)
        
        # return ans

        n = len(boxes)
        left_operations = [0] * n
        right_operations = [0] * n
        
        # Prefix calculation (left to right)
        prefix_sum = 0
        prefix_count = 0
        for i in range(n):
            left_operations[i] = prefix_sum
            if boxes[i] == "1":
                prefix_count += 1
            prefix_sum += prefix_count  # Accumulate moves for the next step

        # Suffix calculation (right to left)
        suffix_sum = 0
        suffix_count = 0
        for j in range(n - 1, -1, -1):
            right_operations[j] = suffix_sum
            if boxes[j] == "1":
                suffix_count += 1
            suffix_sum += suffix_count  # Accumulate moves for the next step

        # Final answer by combining left and right operations
        return [left_operations[i] + right_operations[i] for i in range(n)]
