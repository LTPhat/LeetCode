// Given a binary tree, find its minimum depth.

// The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

// Note: A leaf is a node with no children.

 

// Example 1:


// Input: root = [3,9,20,null,null,15,7]
// Output: 2
// Example 2:

// Input: root = [2,null,3,null,4,null,5,null,6]
// Output: 5

/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */

// DFS

/**
 * @param {TreeNode} root
 * @return {number}
 */
var minDepth = function(root) {
    if (root === null) return 0
    let left = minDepth(root.left)
    let right = minDepth(root.right)
    if (root.left && root.right) return Math.min(left + 1, right + 1)
    return Math.max(left + 1, right + 1)
};


// BFS

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
var minDepth = function(root) {
    if (root === null) return 0
    let depth = 0
    let queue = [root]
    while (queue.length){
        depth += 1
        let n = queue.length
        for (let i = 0; i < n; i ++){
            let item = queue.shift()
            if (item.left == null && item.right == null) return depth
            if (item.left) queue.push(item.left)
            if(item.right) queue.push(item.right)
        }
    }
    return depth
};