# Given the root of a binary tree, flatten the tree into a "linked list":

# The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
# The "linked list" should be in the same order as a pre-order traversal of the binary tree.
 

# Example 1:


# Input: root = [1,2,5,3,4,null,6]
# Output: [1,null,2,null3,null,4,null,5,null,6]
# Example 2:

# Input: root = []
# Output: []
# Example 3:

# Input: root = [0]
# Output: [0]

#Algorithm:
# 1)Check if root is none. If yes, return root, else:
# 2)Check if root.left is none. If yes, move to root.right, else:

# 3)Find the rightmost node of the left subtree of root
# 4)Store the right subtree of root
# 5)Link root.right to root.left, link the rightmost node of left subtree to the right subtree of root stored.
# 6)Return to step 1
# 7)End



class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flatten(self, root):
        #Function to find the rightmost node of leftsubtree
        def findrightmost(root):
            if root.right:
                return findrightmost(root.right)
            return root
        if root == None:
            return root
        else:
            store_right = None
            rightmost = None
            while root:
                if root.left == None:
                    root = root.right
                else:
                    rightmost = findrightmost(root.left)
                    store_right = root.right
                    root.right = root.left
                    root.left = None
                    rightmost.right = store_right
        return list(root)
                    
                    
                    
       
