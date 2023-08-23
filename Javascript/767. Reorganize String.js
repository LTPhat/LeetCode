// Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

// Return any possible rearrangement of s or return "" if not possible.

 

// Example 1:

// Input: s = "aab"
// Output: "aba"
// Example 2:

// Input: s = "aaab"
// Output: ""
 

// Constraints:

// 1 <= s.length <= 500
// s consists of lowercase English letters.




/**
 * @param {string} s
 * @return {string}
 */
var reorganizeString = function(s) {
    let ans = new Array(s.length).fill(0);
        let freMap = {};
        
        for (let i = 0; i < s.length; i++) {
            freMap[s[i]] = (freMap[s[i]] || 0) + 1;
        }
        
        let sortedMap = Object.entries(freMap).sort((a, b) => b[1] - a[1]);
        
        if (sortedMap[0][1] > Math.floor((s.length + 1) / 2)) {         // Key
            return "";
        }
        
        let i = 0;
        for (const [c, value] of sortedMap) {
            for (let j = 0; j < value; j++) {
                if (i >= s.length) {
                    i = 1;
                }
                ans[i] = c;
                i += 2;
            }
        }
        
        return ans.join('');
};