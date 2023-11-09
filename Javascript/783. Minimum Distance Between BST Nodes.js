// Given the root of a Binary Search Tree (BST), return the minimum difference between the values of any two different nodes in the tree.

 

// Example 1:


// Input: root = [4,2,6,1,3]
// Output: 1
// Example 2:


// Input: root = [1,0,48,null,null,12,49]
// Output: 1
 

// Constraints:

// The number of nodes in the tree is in the range [2, 100].
// 0 <= Node.val <= 105

//Approach: Inorder BST tree traversal


// Solution 1

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
var minDiffInBST = function(root) {
    let list = new Array();
    function solve(list){
        let ans = Number.MAX_SAFE_INTEGER;
        for(let i = 0; i < list.length - 1; i++){
            ans = Math.min(ans, list[i+1] - list[i]);
        }
        return ans;
    }
    function inOrderTraversal(root, list){
        if(!root) return;
        inOrderTraversal(root.left, list);
        list.push(root.val);
        inOrderTraversal(root.right, list);
        return list;
    }
    inOrderTraversal(root, list);
    return solve(list);
};



// Solution 2: Remember previous node of every node through traversal


let ans = Number.MAX_SAFE_INTEGER;
    let prev = -1;
    function inOrderTraversal(root){
        if(root.left) inOrderTraversal(root.left);
        if(prev >= 0) ans = Math.min(ans, root.val - prev);
        prev = root.val;
        if(root.right) inOrderTraversal(root.right);
        return ans; 
    }
    return inOrderTraversal(root);