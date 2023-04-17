# You are given a rectangular cake of size h x w and two arrays of integers horizontalCuts and verticalCuts where:

# horizontalCuts[i] is the distance from the top of the rectangular cake to the ith horizontal cut and similarly, and
# verticalCuts[j] is the distance from the left of the rectangular cake to the jth vertical cut.
# Return the maximum area of a piece of cake after you cut at each horizontal and vertical position provided in the arrays horizontalCuts and verticalCuts. Since the answer can be a large number, return this modulo 109 + 7.

 

# Example 1:


# Input: h = 5, w = 4, horizontalCuts = [1,2,4], verticalCuts = [1,3]
# Output: 4 
# Explanation: The figure above represents the given rectangular cake. Red lines are the horizontal and vertical cuts. After you cut the cake, the green piece of cake has the maximum area.
# Example 2:


# Input: h = 5, w = 4, horizontalCuts = [3,1], verticalCuts = [1]
# Output: 6
# Explanation: The figure above represents the given rectangular cake. Red lines are the horizontal and vertical cuts. After you cut the cake, the green and yellow pieces of cake have the maximum area.
# Example 3:

# Input: h = 5, w = 4, horizontalCuts = [3], verticalCuts = [3]
# Output: 9

class Solution(object):
    def maxArea(self, h, w, horizontalCuts, verticalCuts):
        """
        :type h: int
        :type w: int
        :type horizontalCuts: List[int]
        :type verticalCuts: List[int]
        :rtype: int
        """
        horizontalCuts.append(0)
        verticalCuts.append(0)
        horizontalCuts.append(h)
        verticalCuts.append(w)
        length = 0
        width = 0
        horizontalCuts.sort()
        verticalCuts.sort()
        for i in range (len(horizontalCuts)-1):
            width = max(width, horizontalCuts[i+1] - horizontalCuts[i])
        for j in range(len(verticalCuts)-1):
            length = max(length,verticalCuts[j+1] - verticalCuts[j])
        ans = length * width
        return ans % (10**9+7)