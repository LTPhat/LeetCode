# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: 3
# Example 2:

# Input: root = [1,null,2]
# Output: 2

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def maxDepth(self, root):
        def height(root):
            if (root == None):
                return -1
            lheight = height(root.left)
            rheight = height(root.right)
            if (lheight > rheight):
                return lheight + 1
            else:
                return rheight + 1
        ans = height(root) + 1
        return ans