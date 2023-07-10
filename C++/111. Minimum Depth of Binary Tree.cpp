// Given a binary tree, find its minimum depth.

// The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

// Note: A leaf is a node with no children.

 

// Example 1:


// Input: root = [3,9,20,null,null,15,7]
// Output: 2
// Example 2:

// Input: root = [2,null,3,null,4,null,5,null,6]
// Output: 5

#include <algorithm>

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int val = 0, TreeNode* left = nullptr, TreeNode* right = nullptr)
        : val(val), left(left), right(right) {}
};

int minDepth(TreeNode* root) {
    if (root == nullptr) {
        return 0;
    }
    
    int left = minDepth(root->left);
    int right = minDepth(root->right);
    
    if (root->left && root->right) {
        return std::min(left + 1, right + 1);
    }
    
    return std::max(left + 1, right + 1);
}


#include <queue>

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int val = 0, TreeNode* left = nullptr, TreeNode* right = nullptr)
        : val(val), left(left), right(right) {}
};

int minDepth(TreeNode* root) {
    if (root == nullptr) {
        return 0;
    }
    
    int depth = 0;
    std::queue<TreeNode*> queue;
    queue.push(root);
    
    while (!queue.empty()) {
        depth++;
        int n = queue.size();
        
        for (int i = 0; i < n; i++) {
            TreeNode* item = queue.front();
            queue.pop();
            
            if (item->left == nullptr && item->right == nullptr) {
                return depth;
            }
            
            if (item->left) {
                queue.push(item->left);
            }
            
            if (item->right) {
                queue.push(item->right);
            }
        }
    }
    
    return depth;
}