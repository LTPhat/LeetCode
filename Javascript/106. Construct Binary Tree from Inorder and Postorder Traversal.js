// Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.

 

// Example 1:


// Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
// Output: [3,9,20,null,null,15,7]
// Example 2:

// Input: inorder = [-1], postorder = [-1]
// Output: [-1]



// Approach: Divide and Conquer

// Create a function called buildTree that takes in two vectors, inorder and postorder, and returns a pointer to the root of the resulting binary tree.
// Initialize an integer variable postorderIndex to postorder.size() - 1. This variable will be used to traverse the postorder vector in reverse order.
// Initialize an empty unordered map called inorderIndexUmp. This map will be used to quickly look up the index of a value in the inorder vector.
// Loop through the inorder vector and insert each value and its index into the inorderIndexUmp map.
// Call a recursive helper function called buildTreeHelper with parameters postorder, 0, and postorder.size() - 1. This function will return the root of the binary tree.



// In the buildTreeHelper function, if left is greater than right, return nullptr.
// Get the root value from the postorder vector using the postorderIndex variable, and decrement postorderIndex.
// Create a new TreeNode with the root value and assign it to a pointer variable called root.
// Get the index of the root value in the inorder vector from the inorderIndexUmp map, and assign it to an integer variable called inorderPivotIndex.
// Recursively call buildTreeHelper with parameters postorder, inorderPivotIndex + 1, and right. Assign the result to root -> right.
// Recursively call buildTreeHelper with parameters postorder, left, and inorderPivotIndex - 1. Assign the result to root -> left.
// Return root.


/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {number[]} inorder
 * @param {number[]} postorder
 * @return {TreeNode}
 */
var buildTree = function(inorder, postorder) {
    const inorder_map = new Map();
    inorder.forEach((value, index) => inorder_map.set(value, index));
    const n = inorder.length;
    let post_index = n - 1;
    return treeBuilder(0, n - 1);
    function treeBuilder(left, right){
        if(post_index < 0 || left > right) return null;

        let curr_val = postorder[post_index--];
        let curr_node = new TreeNode(curr_val);
        let curr_index = inorder_map.get(curr_val);
        curr_node.right = treeBuilder(curr_index + 1, right);
        curr_node.left = treeBuilder(left, curr_index - 1);

        return curr_node; 
    }
};


