# Given the root of a binary tree, return the same tree where every subtree (of the given tree) not containing a 1 has been removed.

# A subtree of a node node is node plus every node that is a descendant of node.

 

# Example 1:


# Input: root = [1,null,0,0,1]
# Output: [1,null,0,null,1]
# Explanation: 
# Only the red nodes satisfy the property "every subtree not containing a 1".
# The diagram on the right represents the answer.
# Example 2:


# Input: root = [1,0,1,0,0,0,1]
# Output: [1,null,1,null,1]
# Example 3:


# Input: root = [1,1,0,1,1,0,1,0]
# Output: [1,1,0,1,1,null,1]
 

# Constraints:

# The number of nodes in the tree is in the range [1, 200].
# Node.val is either 0 or 1.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pruneTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if root is None:
            return None
        if self.pruneTree(root.left) is None:
            root.left = None
        if self.pruneTree(root.right) is None:
            root.right = None
        if root.val != 1 and root.left is None and root.right is None:
            root = None
        return root
            