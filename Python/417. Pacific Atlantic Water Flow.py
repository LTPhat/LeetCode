# There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

# The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

# The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

# Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

 

# Example 1:


# Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
# Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
# Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
# [0,4]: [0,4] -> Pacific Ocean 
#        [0,4] -> Atlantic Ocean
# [1,3]: [1,3] -> [0,3] -> Pacific Ocean 
#        [1,3] -> [1,4] -> Atlantic Ocean
# [1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean 
#        [1,4] -> Atlantic Ocean
# [2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean 
#        [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
# [3,0]: [3,0] -> Pacific Ocean 
#        [3,0] -> [4,0] -> Atlantic Ocean
# [3,1]: [3,1] -> [3,0] -> Pacific Ocean 
#        [3,1] -> [4,1] -> Atlantic Ocean
# [4,0]: [4,0] -> Pacific Ocean 
#        [4,0] -> Atlantic Ocean
# Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.
# Example 2:

# Input: heights = [[1]]
# Output: [[0,0]]
# Explanation: The water can flow from the only cell to the Pacific and Atlantic oceans.

class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        rows, cols = len(heights),len(heights[0])
        ans = []
        pacific, atlantic = set(),set()
        # Depth first search function
        def dfs(r, c, visited, preheight):
            if ((r,c) in visited or r < 0 or c < 0 
                or r==rows or c==cols or heights[r][c] < preheight):
                return 
            visited.add((r,c))
            direction = [[1,0],[-1,0],[0,1],[0,-1]]
            for i, j in direction:
                dfs(r+i,c+j,visited,heights[r][c])
        #Check first row (pacific) and last row(atlantic)
        for c in range(cols):
            dfs(0, c, pacific, heights[0][c]) #Check first row
            dfs(rows-1, c, atlantic, heights[rows-1][c])
        #Check first column (pacific) and last column(atlantic)
        for r in range(rows):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, cols-1,atlantic, heights[r][cols-1])
        #Add elements in both alantic and pacific to ans
        for row in range(rows):
            for col in range(cols):
                if (row,col) in pacific and (row,col) in atlantic:
                    ans.append([row,col])
        return ans
        
            
        