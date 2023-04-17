/**
 * @param {number} n
 * @return {number}
 */
var getMaximumGenerated = function(n) {
    if (n === 0) return 0;
    if (n === 1) return 1;
    let nums = [0, 1];
    for (let i = 2; i <= n; i++){
        if (i % 2 === 0){
            nums.push(nums[i / 2]);
        }else{
            nums.push(nums[parseInt(i / 2)] + nums[parseInt(i / 2) + 1] );
        }
    }
    return Math.max(...nums);
};