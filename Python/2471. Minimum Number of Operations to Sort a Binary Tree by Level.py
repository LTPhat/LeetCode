# You are given the root of a binary tree with unique values.

# In one operation, you can choose any two nodes at the same level and swap their values.

# Return the minimum number of operations needed to make the values at each level sorted in a strictly increasing order.

# The level of a node is the number of edges along the path between it and the root node.

 

# Example 1:


# Input: root = [1,4,3,7,6,8,5,null,null,null,null,9,null,10]
# Output: 3
# Explanation:
# - Swap 4 and 3. The 2nd level becomes [3,4].
# - Swap 7 and 5. The 3rd level becomes [5,6,8,7].
# - Swap 8 and 7. The 3rd level becomes [5,6,7,8].
# We used 3 operations so return 3.
# It can be proven that 3 is the minimum number of operations needed.
# Example 2:


# Input: root = [1,3,2,7,6,5,4]
# Output: 3
# Explanation:
# - Swap 3 and 2. The 2nd level becomes [2,3].
# - Swap 7 and 4. The 3rd level becomes [4,6,5,7].
# - Swap 6 and 5. The 3rd level becomes [4,5,6,7].
# We used 3 operations so return 3.
# It can be proven that 3 is the minimum number of operations needed.
# Example 3:


# Input: root = [1,2,3,4,5,6]
# Output: 0
# Explanation: Each level is already sorted in increasing order so return 0.
 

# Constraints:

# The number of nodes in the tree is in the range [1, 105].
# 1 <= Node.val <= 105
# All the values of the tree are unique.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minimumOperations(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def get_min_swap(arr):
            n = len(arr)
            swaps = 0

            # Pair elements with their indices and sort based on values
            arr_pos = [(val, idx) for idx, val in enumerate(arr)]
            arr_pos.sort(key=lambda x: x[0])

            # Track visited elements
            visited = [False] * n

            for i in range(n):
                # Skip if element is already visited or in correct position
                if visited[i] or arr_pos[i][1] == i:
                    continue

                # Find the size of the cycle
                cycle_size = 0
                j = i
                while not visited[j]:
                    visited[j] = True
                    j = arr_pos[j][1]
                    cycle_size += 1

                # Add swaps required for the cycle
                if cycle_size > 1:
                    swaps += (cycle_size - 1)

            return swaps

        total_swap = 0
        queue = [root]

        while queue:
            level_size = len(queue)
            level_array = []

            for _ in range(level_size):
                node = queue.pop(0)
                level_array.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            total_swap += get_min_swap(level_array)
        
        return total_swap