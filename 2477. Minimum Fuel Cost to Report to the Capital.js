// There is a tree (i.e., a connected, undirected graph with no cycles) structure country network consisting of n cities numbered from 0 to n - 1 and exactly n - 1 roads. The capital city is city 0. You are given a 2D integer array roads where roads[i] = [ai, bi] denotes that there exists a bidirectional road connecting cities ai and bi.

// There is a meeting for the representatives of each city. The meeting is in the capital city.

// There is a car in each city. You are given an integer seats that indicates the number of seats in each car.

// A representative can use the car in their city to travel or change the car and ride with another representative. The cost of traveling between two cities is one liter of fuel.

// Return the minimum number of liters of fuel to reach the capital city.


/**
 * @param {number[][]} roads
 * @param {number} seats
 * @return {number}
 */
var minimumFuelCost = function(roads, seats) {
    const adjList = Array.from({length: roads.length + 1}, ()=>[])
    for (const [from, to] of roads) {
        adjList[from].push(to);
        adjList[to].push(from);
    }
    let ans = 0;
    const dfs = (node, p) => {
        let here = 1;
        for (const ne of adjList[node]) {
            if (ne != p) {
                here += dfs(ne, node);
            }
        }
        if (p !== -1) {
            ans += Math.ceil(here / seats);
        } else {
        return ans;
        }
        return here;
    };
    return dfs(0, -1);
};