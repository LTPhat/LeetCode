// You are the manager of a basketball team. For the upcoming tournament, you want to choose the team with the highest overall score. The score of the team is the sum of scores of all the players in the team.

// However, the basketball team is not allowed to have conflicts. A conflict exists if a younger player has a strictly higher score than an older player. A conflict does not occur between players of the same age.

// Given two lists, scores and ages, where each scores[i] and ages[i] represents the score and age of the ith player, respectively, return the highest overall score of all possible basketball teams.

 

// Example 1:

// Input: scores = [1,3,5,10,15], ages = [1,2,3,4,5]
// Output: 34
// Explanation: You can choose all the players.
// Example 2:

// Input: scores = [4,5,6,5], ages = [2,1,2,1]
// Output: 16
// Explanation: It is best to choose the last 3 players. Notice that you are allowed to choose multiple people of the same age.
// Example 3:

// Input: scores = [1,2,3,5], ages = [8,9,10,1]
// Output: 6
// Explanation: It is best to choose the first 3 players. 

// Giải thuật: Dynamic Programing

// 1) Tạo mảng ageScore chứa các phần tử là điểm và tuổi tương ứng của phần từ thứ i
// 2) Sort mảng ageScore theo thứ tự giảm dần theo thứ tự ưu tiên lần lượt là tuổi, sau đó đến điểm
// 3) Gọi mảng dp với dp[i] là điểm số tối đa của team có thể có sau khi duyệt qua phần tử thứ i của ageScore sau khi sort.
// 4) Với mỗi i, đầu tiên đặt dp[i] là điểm của phần tử i, duyệt mảng ageScore theo biến j từ 0 đến i-1, chỉ xét những phần tử có điểm số >= điểm của phần tử thứ i
//  Dp equaation: dp[i] = max(dp[i], dp[j] + ageScore[i][0])

// Time complexity: O(n^2)

/**
 * @param {number[]} scores
 * @param {number[]} ages
 * @return {number}
 */
var bestTeamScore = function(scores, ages) {
    const n = scores.length;
    let ageScore = new Array;
    for (let i = 0; i < n; i++){
        ageScore.push([scores[i], ages[i]]);
    }
    ageScore.sort((x, y)=>{
        if (x[1] === y[1]){
            return y[0] - x[0];
        }
        return y[1] - x[1];
    });
    let dp = new Array(n).fill(0);
    for (let i = 0; i < n; i++){
        dp[i] = ageScore[i][0];
        for (let j = 0; j < i; j++){
            if(ageScore[j][0] >= ageScore[i][0]){
                dp[i] = Math.max(dp[i], dp[j] + ageScore[i][0]);
            }
        }
    }
    return Math.max(...dp);
};