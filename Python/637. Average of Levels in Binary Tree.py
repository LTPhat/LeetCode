# Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10-5 of the actual answer will be accepted.
 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: [3.00000,14.50000,11.00000]
# Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
# Hence return [3, 14.5, 11].
# Example 2:


# Input: root = [3,9,20,15,7]
# Output: [3.00000,14.50000,11.00000]
 

# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# -231 <= Node.val <= 231 - 1
# Definition for a binary tree node.
from collections import defaultdict
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        value_list = defaultdict(float)
        value_count = defaultdict(int)
        def dfs(node, height):
            if not node: return
            value_list[height] += node.val
            value_count[height] += 1
            dfs(node.left, height+1)
            dfs(node.right,height+1)
        dfs(root,0)
        ans = [value_list[i]/value_count[i] for i in range(len(value_list))]
        return ans
        
        