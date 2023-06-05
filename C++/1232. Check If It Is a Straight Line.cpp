// You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.


#include<iostream>
#include<algorithm>
#include<math.h>
#include<vector>
using namespace std;

class Solution {
public:
    bool checkStraightLine(vector<vector<int>>& coordinates) {
        int x0 = coordinates[0][0];
        int y0 = coordinates[0][1];
        int x1 = coordinates[1][0];
        int y1 = coordinates[1][1];
        for (const auto& coord : coordinates) {
            int x = coord[0];
            int y = coord[1];
            if ((y - y0) * (x1 - x0) != (x - x0) * (y1 - y0)) {
                return false;
            }
        }
        return true;
    }
};