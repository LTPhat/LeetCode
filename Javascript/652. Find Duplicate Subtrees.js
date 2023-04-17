// Given the root of a binary tree, return all duplicate subtrees.

// For each kind of duplicate subtrees, you only need to return the root node of any one of them.

// Two trees are duplicate if they have the same structure with the same node values.

 

// Example 1:


// Input: root = [1,2,3,4,null,2,4,null,null,4]
// Output: [[2,4],[4]]
// Example 2:


// Input: root = [2,1,1]
// Output: [[1]]
// Example 3:


// Input: root = [2,2,2,3,null,3,null]
// Output: [[2,3],[3]]


// Approach: DFS - Preorder Traversal

// At each node, create a string representation the subtree which that node is the root, which consist of [node.val, path(node.left), path(node.right))]
// Store the path and the frenquency in a hashmap, if hashmap[path] == 2, there are two similar subtree of the original tree, so add the node of that path to res.




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
 * @return {TreeNode[]}
 */
var findDuplicateSubtrees = function(root) {
    let hash_map = {};
    let res = [];
    function dfs(node, path){
        if (!node) return "#";
        let left_path = dfs(node.left, path);
        let right_path = dfs(node.right, path);
        path += [node.val, left_path, right_path].join(",");
        if (!hash_map[path]){
            hash_map[path] = 1;
        }else{
            hash_map[path] += 1;
        }
        if (hash_map[path] == 2){
            res.push(node);
        }
        return path;
    }
    dfs(root, "");
    return res;
};