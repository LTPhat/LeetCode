// Given an integer n, return all the structurally unique BST's (binary search trees), which has exactly n nodes of unique values from 1 to n. Return the answer in any order.

 

// Example 1:


// Input: n = 3
// Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]
// Example 2:

// Input: n = 1
// Output: [[1]]


/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {number} n
 * @return {TreeNode[]}
 */
var generateTrees = function(n) {
    function dfs(nums) {
      if (!nums.length) {
        return [null];
      }
      const ans = [];
      for (let i = 0; i < nums.length; i++) {
        const leftTree = dfs(nums.slice(0, i));
        const rightTree = dfs(nums.slice(i + 1));
        for (const l of leftTree) {
          for (const r of rightTree) {
            const root = new TreeNode(nums[i]);
            root.left = l;
            root.right = r;
            ans.push(root);
          }
        }
      }
      return ans;
    }

    const nums = Array.from({ length: n }, (_, i) => i + 1);
    return dfs(nums);
};

