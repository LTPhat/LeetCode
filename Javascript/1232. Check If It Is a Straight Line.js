// You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.

 

 

// Example 1:



// Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
// Output: true
// Example 2:



// Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
// Output: false


/**
 * @param {number[][]} coordinates
 * @return {boolean}
 */
var checkStraightLine = function(coordinates) {
    let [x0, y0] = coordinates[0]
    let [x1, y1] = coordinates[1]
    for (let [x,y] of coordinates){
        if ((y - y0) * (x1 - x0) !== (x - x0) * (y1 - y0)){
            return false
        }
    }
    return true;
};