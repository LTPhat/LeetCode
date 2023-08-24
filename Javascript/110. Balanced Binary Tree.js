// Given a binary tree, determine if it is 
// height-balanced
// .

 

// Example 1:


// Input: root = [3,9,20,null,null,15,7]
// Output: true
// Example 2:


// Input: root = [1,2,2,3,3,null,null,4,4]
// Output: false
// Example 3:

// Input: root = []
// Output: true
 

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
 * @return {boolean}
 */
var isBalanced = function(root) {
    function height(node){
        if (!node){
            return 0
        }
        let leftHeight = height(node.left)
        let rightHeight = height(node.right)
        if (leftHeight === -1 || rightHeight === -1){
            return -1
        }
        if (Math.abs(leftHeight - rightHeight) > 1){
            return -1
        }
        return 1 + Math.max(leftHeight, rightHeight)
    }
    return height(root)=== -1 ? false: true
    
};