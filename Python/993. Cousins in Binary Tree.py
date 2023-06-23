# Given the root of a binary tree with unique values and the values of two different nodes of the tree x and y, return true if the nodes corresponding to the values x and y in the tree are cousins, or false otherwise.

# Two nodes of a binary tree are cousins if they have the same depth with different parents.

# Note that in a binary tree, the root node is at the depth 0, and children of each depth k node are at the depth k + 1.

 

# Example 1:


# Input: root = [1,2,3,4], x = 4, y = 3
# Output: false
# Example 2:


# Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
# Output: true
# Example 3:


# Input: root = [1,2,3,null,4], x = 2, y = 3
# Output: false


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        # queue = [[node, its parent, its level]]
        queue = [[root, None , 0]]
        level = 0
        xParent = None
        yParent = None
        while len(queue):
            n = len(queue)
            level += 1
            for i in range(0, n):
                item = queue.pop(0)
                if (x == item[0].val):
                    xParent, xLevel = item[1], item[2]
                elif (y == item[0].val):
                    yParent, yLevel = item[1], item[2]
                if xParent and yParent:
                    return xParent != yParent and xLevel == yLevel
                if item[0].left:
                    queue.append([item[0].left, item[0].val, level])
                if item[0].right:
                    queue.append([item[0].right, item[0].val, level])
        return False
                