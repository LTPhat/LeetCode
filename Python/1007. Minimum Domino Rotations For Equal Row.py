# In a row of dominoes, tops[i] and bottoms[i] represent the top and bottom halves of the ith domino. (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

# We may rotate the ith domino, so that tops[i] and bottoms[i] swap values.

# Return the minimum number of rotations so that all the values in tops are the same, or all the values in bottoms are the same.

# If it cannot be done, return -1.

 

# Example 1:


# Input: tops = [2,1,2,4,2,2], bottoms = [5,2,6,2,3,2]
# Output: 2
# Explanation: 
# The first figure represents the dominoes as given by tops and bottoms: before we do any rotations.
# If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2, as indicated by the second figure.
# Example 2:

# Input: tops = [3,5,1,2,3], bottoms = [3,6,3,3,4]
# Output: -1
# Explanation: 
# In this case, it is not possible to rotate the dominoes to make one row of values equal.


class Solution(object):
    def minDominoRotations(self, tops, bottoms):
        """
        :type tops: List[int]
        :type bottoms: List[int]
        :rtype: int
        """
        n = len(tops)
        min_rotations = float('inf')
        # Potential target values are the values of the first domino
        potential_targets = [tops[0], bottoms[0]]
        for target in potential_targets:
            possible = True
            top_rotations = 0
            # Check if it's possible to make all tops equal to target
            for i in range(n):
                if tops[i] == target:
                    continue # Already has target on top
                elif bottoms[i] == target:
                    top_rotations += 1 # rotate this domino
                else:
                    possible = False   #Can't make this domino have target on top
                    break
            if possible:
                min_rotations = min(min_rotations, top_rotations)
            
            possible = True
            bottom_rotations = 0
            # Check if it's possible to make all bottoms equal to target
            for i in range(n):
                if bottoms[i] == target:
                    continue
                elif tops[i] == target:
                    bottom_rotations += 1
                else:
                    possible = False
                    break
            if possible:
                min_rotations = min(min_rotations, bottom_rotations)
        
        return min_rotations if min_rotations != float('inf') else -1
            