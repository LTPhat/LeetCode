# Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.

 

# Example 1:


# Input: root = [4,2,6,1,3]
# Output: 1
# Example 2:

import sys

# Input: root = [1,0,48,null,null,12,49]
# Output: 1

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def inorderTraverse(root):
            if not root: 
                return
            inorderTraverse(root.left)
            inorderList.append(root.val)
            inorderTraverse(root.right)
        inorderList = []
        minAbs = sys.maxint
        inorderTraverse(root)
        for i in range(1, len(inorderList)):
            minAbs = min(minAbs, abs(inorderList[i] - inorderList[i - 1]))
        return minAbs
