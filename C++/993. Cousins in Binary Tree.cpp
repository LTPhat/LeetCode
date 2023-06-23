// Given the root of a binary tree with unique values and the values of two different nodes of the tree x and y, return true if the nodes corresponding to the values x and y in the tree are cousins, or false otherwise.

// Two nodes of a binary tree are cousins if they have the same depth with different parents.

// Note that in a binary tree, the root node is at the depth 0, and children of each depth k node are at the depth k + 1.

 

// Example 1:


// Input: root = [1,2,3,4], x = 4, y = 3
// Output: false
// Example 2:


// Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
// Output: true
// Example 3:


// Input: root = [1,2,3,null,4], x = 2, y = 3
// Output: false


//Definition for a binary tree node.
struct TreeNode {
        int val;
        TreeNode *left;
        TreeNode *right;
        TreeNode() : val(0), left(nullptr), right(nullptr) {}
        TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
        TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

#include <iostream>
#include <queue>

class Solution {
public:
    bool isCousins(TreeNode* root, int x, int y) {
        std::queue<std::tuple<TreeNode*, TreeNode*, int>> queue;
        queue.push(std::make_tuple(root, nullptr, 0));
        int level = 0;
        TreeNode* xParent = nullptr;
        TreeNode* yParent = nullptr;
        int xLevel  = 0;
        int yLevel = 0;
        while (!queue.empty()) {
            int n = queue.size();
            level++;
            for (int i = 0; i < n; i++) {
                auto item = queue.front();
                queue.pop();
                TreeNode* node = std::get<0>(item);
                TreeNode* parent = std::get<1>(item);
                int nodeLevel = std::get<2>(item);
                if (node->val == x) {
                    xParent = parent;
                    xLevel = level;
                } else if (node->val == y) {
                    yParent = parent;
                    yLevel = level;
                }
                if (xParent && yParent) {
                    return xParent != yParent && xLevel == yLevel;
                }
                if (node->left) {
                    queue.push(std::make_tuple(node->left, node, level));
                }
                if (node->right) {
                    queue.push(std::make_tuple(node->right, node, level));
                }
            }
        }
        return false;
    }
};