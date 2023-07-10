// Given the root of a binary tree, return all root-to-leaf paths in any order.

// A leaf is a node with no children.

 

// Example 1:


// Input: root = [1,2,3,null,5]
// Output: ["1->2->5","1->3"]
// Example 2:

// Input: root = [1]
// Output: ["1"]

#include <string>
#include <vector>

#include <string>
#include <vector>

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int val = 0, TreeNode* left = nullptr, TreeNode* right = nullptr)
        : val(val), left(left), right(right) {}
};

void traverse(TreeNode* root, std::string path, std::vector<std::string>& paths) {
    path += std::to_string(root->val);
    
    if (root->left == nullptr && root->right == nullptr) {
        paths.push_back(path);
        return;
    }
    
    if (root->left) {
        traverse(root->left, path + "->", paths);
    }
    
    if (root->right) {
        traverse(root->right, path + "->", paths);
    }
}

std::vector<std::string> binaryTreePaths(TreeNode* root) {
    std::vector<std::string> paths;
    
    if (root == nullptr) {
        return paths;
    }
    
    traverse(root, "", paths);
    
    return paths;
}