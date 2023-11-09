/**
 * @param {number} num
 * @return {number}
 */
var splitNum = function(num) {
    let num_str = num.toString().split('').sort((x, y) =>{
        return parseInt(x) - parseInt(y);
    })
    num_str = num_str.join('');
    let num1_str = '';
    let num2_str = '';
    for (let i = 0; i < num_str.length; i++){
        if (i % 2 === 1){
            num1_str += num_str[i];
        }else{
            num2_str += num_str[i];
        }
    }
    return parseInt(num1_str) + parseInt(num2_str);
};