// Given an integer n, return all the structurally unique BST's (binary search trees), which has exactly n nodes of unique values from 1 to n. Return the answer in any order.

 

// Example 1:


// Input: n = 3
// Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]
// Example 2:

// Input: n = 1
// Output: [[1]]
 

// Constraints:

// 1 <= n <= 8


#include <iostream>
#include <vector>
using namespace std;



// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int val = 0, TreeNode* left = nullptr, TreeNode* right = nullptr)
        : val(val), left(left), right(right) {}
};

std::vector<TreeNode*> generateTrees(int n) {
    if (n == 0) {
        return std::vector<TreeNode*>();
    }

    std::function<std::vector<TreeNode*>(int, int)> dfs = [&](int start, int end) {
        std::vector<TreeNode*> ans;

        if (start > end) {
            ans.push_back(nullptr);
            return ans;
        }

        for (int i = start; i <= end; ++i) {
            std::vector<TreeNode*> leftTree = dfs(start, i - 1);
            std::vector<TreeNode*> rightTree = dfs(i + 1, end);

            for (auto& left : leftTree) {
                for (auto& right : rightTree) {
                    TreeNode* root = new TreeNode(i);
                    root->left = left;
                    root->right = right;
                    ans.push_back(root);
                }
            }
        }

        return ans;
    };

    return dfs(1, n);
}