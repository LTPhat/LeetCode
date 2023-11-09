// Given the root of a binary tree, return its maximum depth.

// A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

// Example 1:


// Input: root = [3,9,20,null,null,15,7]
// Output: 3
// Example 2:

// Input: root = [1,null,2]
// Output: 2


// Recursive call
// Find the max-height of the left subtree and max-height of right-subtree
// Return the larger value


/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var maxDepth = function(root) {
    function getHeight(root){
         if (!root){
             return 0;
     }
         let rightHeight = maxDepth(root.right);
         let leftHeight = maxDepth(root.left);
         if(rightHeight > leftHeight){
             return rightHeight + 1;
         }else{
             return leftHeight + 1;
         }
    }
    return getHeight(root);
 };