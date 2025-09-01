# There is a school that has classes of students and each class will be having a final exam. You are given a 2D integer array classes, where classes[i] = [passi, totali]. You know beforehand that in the ith class, there are totali total students, but only passi number of students will pass the exam.

# You are also given an integer extraStudents. There are another extraStudents brilliant students that are guaranteed to pass the exam of any class they are assigned to. You want to assign each of the extraStudents students to a class in a way that maximizes the average pass ratio across all the classes.

# The pass ratio of a class is equal to the number of students of the class that will pass the exam divided by the total number of students of the class. The average pass ratio is the sum of pass ratios of all the classes divided by the number of the classes.

# Return the maximum possible average pass ratio after assigning the extraStudents students. Answers within 10-5 of the actual answer will be accepted.

 

# Example 1:

# Copy to BlackBox
# Input: classes = [[1,2],[3,5],[2,2]], extraStudents = 2
# Output: 0.78333
# Explanation: You can assign the two extra students to the first class. The average pass ratio will be equal to (3/4 + 3/5 + 2/2) / 3 = 0.78333.
# Example 2:

# Copy to BlackBox
# Input: classes = [[2,4],[3,9],[4,5],[2,10]], extraStudents = 4
# Output: 0.53485

import heapq

class Solution(object):
    def maxAverageRatio(self, classes, extraStudents):
        def calculate_gain(pass_i, total_i):
            return ((pass_i + 1) * 1.0) / (total_i * 1.0 + 1) - (pass_i* 1.0) / (total_i * 1.0)
        
        max_heap = []
        for pass_i, total_i in classes:
            heapq.heappush(max_heap, (-calculate_gain(pass_i, total_i), pass_i, total_i))
        # Add each extra to student to the class that has largest gain
        for _ in range(extraStudents):
            _, pass_i, total_i = heapq.heappop(max_heap)
            pass_i += 1
            total_i += 1
            heapq.heappush(max_heap, (-calculate_gain(pass_i, total_i), pass_i, total_i))  # Max-heap (default min-heap)
        
        avg_pass_ratio = 0
        while max_heap:
            _, pass_i, total_i = heapq.heappop(max_heap)
            avg_pass_ratio += (pass_i * 1.0) / total_i
        
        return avg_pass_ratio / float(len(classes))
