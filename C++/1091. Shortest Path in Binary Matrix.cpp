// Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

// A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

// All the visited cells of the path are 0.
// All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
// The length of a clear path is the number of visited cells of this path.

#include<iostream>
#include<algorithm>
#include<string>
#include<vector>
#include<deque>

using namespace std;


class Solution {
public:
    int shortestPathBinaryMatrix(vector<vector<int>>& grid) {
        int n = grid.size();
        if (grid[0][0] || grid[n - 1][n - 1]) return -1;
        auto invalid = [](int row, int col, int n) {
            return row < 0 || col < 0 || row == n || col == n;
        };
        vector<vector<int>> directions = {
        {1, 0},
        {-1, 0},
        {0, 1},
        {0, -1},
        {1, 1},
        {1, -1},
        {-1, 1},
        {-1, -1}
        };
        deque <vector<int>> deque;
        deque.push_back({0, 0, 1});


        while(!deque.empty()){
            vector<int> curr = deque.front();
            deque.pop_front();
            int row = curr[0];
            int col = curr[1];
            int dis = curr[2];
            if (row == n - 1 && col == n - 1) return dis;
            
            for(const vector<int>& dir : directions){
                int currX = row + dir[0];
                int currY = col + dir[1];
                if (currX < 0 || currX >= n || currY < 0 || currY >= n) continue;
                if (grid[currX][currY] != 0) continue;
                grid[currX][currY] = 1;
                deque.push_back({currX, currY, dis + 1});
            }
        }

        return -1;
    }
};