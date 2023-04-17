# Return the maximum product of the sums of the two subtrees. Since the answer may be too large, return it modulo 109 + 7.

# Note that you need to maximize the answer before taking the mod and not after taking it.

 

# Example 1:


# Input: root = [1,2,3,4,5,6]
# Output: 110
# Explanation: Remove the red edge and get 2 binary trees with sum 11 and 10. Their product is 110 (11*10)
# Example 2:


# Input: root = [1,null,2,3,4,null,null,5,6]
# Output: 90
# Explanation: Remove the red edge and get 2 binary trees with sum 15 and 6.Their product is 90 (15*6)
 

# Constraints:

# The number of nodes in the tree is in the range [2, 5 * 104].
# 1 <= Node.val <= 104

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Calculate sum of every subtree which head is any of node in the main tree, store in subtree_sum
# Find max product
from numpy import inf
class Solution(object):
    def maxProduct(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        subtree_sum = []
        def subtreeSum(rootnode):
            """
            Calculate sum of subtree which head is root
            """
            if rootnode is None:
                return 0
            ans = rootnode.val + subtreeSum(rootnode.left) + subtreeSum(rootnode.right)
            subtree_sum.append(ans)
            return ans
        ans = -float('inf')
        sum_main_tree = subtreeSum(root)
        for val in subtree_sum:
            ans = max(ans, (sum_main_tree - val)*val) 
        return ans % (pow(10,9)+7)
        