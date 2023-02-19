// Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

 

// Example 1:


// Input: root = [3,9,20,null,null,15,7]
// Output: [[3],[20,9],[15,7]]
// Example 2:

// Input: root = [1]
// Output: [[1]]
// Example 3:

// Input: root = []
// Output: []


// Approach: Breadth First Search
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
 * @return {number[][]}
 */
var zigzagLevelOrder = function(root) {
    if (!root) return [];
    let queue = [root];
    let left_to_right = true;
    let ans = [];
    while (queue.length){
        let curr_level = [];
        let size = queue.length;
        for (let i = 0; i < size; i++){
            let node = queue.shift();
            curr_level.push(node.val);
            if (node.left){
                queue.push(node.left);
            }
            if (node.right){
                queue.push(node.right);
            }
        }
        if (left_to_right){
            left_to_right = false;
        }else{
            left_to_right = true;
            curr_level = curr_level.reverse();
        }
        ans.push(curr_level);
    }
    return ans;
};