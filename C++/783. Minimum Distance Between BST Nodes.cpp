// Given the root of a Binary Search Tree (BST), return the minimum difference between the values of any two different nodes in the tree.

 

// Example 1:


// Input: root = [4,2,6,1,3]
// Output: 1
// Example 2:


// Input: root = [1,0,48,null,null,12,49]
// Output: 1
 

// Constraints:

// The number of nodes in the tree is in the range [2, 100].
// 0 <= Node.val <= 105
 

 
// Definition for a binary tree node.

  struct TreeNode {
      int val;
     TreeNode *left;
     TreeNode *right;
     TreeNode() : val(0), left(nullptr), right(nullptr) {}
     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
      TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 };
 #include<iostream>
 #include<algorithm>
 #include<vector>
 using namespace std;
 


class Solution {
public:
    vector <int> list;
    void inorderTraverse(TreeNode *root){
        if (root == nullptr){
            return;
        }
        else{
            inorderTraverse(root->left);
            list.push_back(root->val);
            inorderTraverse(root->right);
        }
    }
    int minDiffInBST(TreeNode* root) {
        if (!root) return 0;
        inorderTraverse(root);
        int minDiff = INT_MAX;
        for (int i = 1; i < list.size(); i++){
            minDiff = min(minDiff, list[i] - list[i - 1]);
        }
        return minDiff;
    }
};