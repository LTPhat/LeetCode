// Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

// Return the smallest level x such that the sum of all the values of nodes at level x is maximal.

 

// Example 1:


// Input: root = [1,7,0,7,-8,null,null]
// Output: 2
// Explanation: 
// Level 1 sum = 1.
// Level 2 sum = 7 + 0 = 7.
// Level 3 sum = 7 + -8 = -1.
// So we return the level with the maximum sum which is level 2.
// Example 2:

// Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
// Output: 2

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
var maxLevelSum = function(root) {
    let queue = [root]
    let maxSum = - Number.MAX_SAFE_INTEGER
    let currLevel = 1
    let maxLevel = 1
    while (queue.length){
        let levelNode = []
        let levelSum = 0
        for (let item of queue){
            levelSum += item.val
            if (item.left){
                levelNode.push(item.left)
            }
            if (item.right){
                levelNode.push(item.right)
            }
        }
        if (levelSum > maxSum){
            maxLevel = currLevel
            maxSum = levelSum
        }
        currLevel += 1
        queue = levelNode
    }
    return maxLevel
};