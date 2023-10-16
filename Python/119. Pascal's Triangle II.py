# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

# Example 1:

# Input: rowIndex = 3
# Output: [1,3,3,1]
# Example 2:

# Input: rowIndex = 0
# Output: [1]
# Example 3:

# Input: rowIndex = 1
# Output: [1,1]


class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        tri = [[1], []]
        for i in range(1, rowIndex + 1):
            curr_row = tri[1]
            prev_row = tri[0]
            for e in range(i + 1):
                if e == 0 or e == i:
                    curr_row.append(1)
                else:
                    curr_row.append(prev_row[e - 1] + prev_row[e])
            tri[0] = tri[1][:]
            tri[1] = []
        return tri[0]  
                
        