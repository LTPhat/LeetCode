// Given a string s, partition s such that every 
// substring
//  of the partition is a 
// palindrome
// . Return all possible palindrome partitioning of s.

 

// Example 1:

// Input: s = "aab"
// Output: [["a","a","b"],["aa","b"]]
// Example 2:

// Input: s = "a"
// Output: [["a"]]


function check_palindrome(s){
    return s === [...s].reverse().join('');
}

var partition = function(s){
    const res = [];
    const n = s.length;
    const backtrack = (i, curr) => {
        if (i === n){
            res.push([...curr]);
        }
        for (let j = i; j < n; j++){
            const to_check = s.substring(i, j+1);
            if (check_palindrome(to_check)){
                curr.push(to_check);
                backtrack(i+1, curr);
                curr.pop();
            }
        }
    }
    backtrack(0, []);
    return res;
}