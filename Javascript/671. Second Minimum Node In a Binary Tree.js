// Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree has exactly two or zero sub-node. If the node has two sub-nodes, then this node's value is the smaller value among its two sub-nodes. More formally, the property root.val = min(root.left.val, root.right.val) always holds.

// Given such a binary tree, you need to output the second minimum value in the set made of all the nodes' value in the whole tree.

// If no such second minimum value exists, output -1 instead.

 

 

// Example 1:


// Input: root = [2,2,5,null,null,5,7]
// Output: 5
// Explanation: The smallest value is 2, the second smallest value is 5.
// Example 2:


// Input: root = [2,2,2]
// Output: -1
// Explanation: The smallest value is 2, but there isn't any second smallest value.


//Approach: Inorder Traversal and save all nodes in array, then find the second minimum element of that array

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
var findSecondMinimumValue = function(root) {
    let list = [];
    function inOrderTraversal(root){
        if (!root) return ;
        inOrderTraversal(root.left);
        list.push(root.val);
        inOrderTraversal(root.right);
    }
    function findSecond(list){
     let smallest = Number.MAX_SAFE_INTEGER;
     for (let i = 0; i < list.length; i++){
         if (list[i] < smallest){
             smallest = list[i];
         }
     }
     let second = Number.MAX_SAFE_INTEGER ;
     for (let j = 0; j < list.length; j++){
         if (list[j] < second && list[j] > smallest){
             second = list[j];
            }
        }
        return second == Number.MAX_SAFE_INTEGER? -1: second;
     }
    inOrderTraversal(root);
    return findSecond(list);
};