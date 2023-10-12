// Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.

 

// Example 1:

// Input: words = ["bella","label","roller"]
// Output: ["e","l","l"]
// Example 2:

// Input: words = ["cool","lock","cook"]
// Output: ["c","o"]
 

// Constraints:

// 1 <= words.length <= 100
// 1 <= words[i].length <= 100
// words[i] consists of lowercase English letters.

/**
 * @param {string[]} words
 * @return {string[]}
 */
var commonChars = function(words) {
    let ans = [];
        let charFreq = {};

        for (let i = 0; i < words.length; i++) {
            const word = words[i];
            for (let j = 0; j < word.length; j++) {
                const char = word[j];
                if (!charFreq[char]) {
                    charFreq[char] = new Array(words.length).fill(0);
                    charFreq[char][i] = 1;
                } else {
                    charFreq[char][i]++;
                }
            }
        }

        for (const char in charFreq) {
            if (charFreq.hasOwnProperty(char)) {
                const minCount = Math.min(...charFreq[char]);
                for (let i = 0; i < minCount; i++) {
                    ans.push(char);
                }
            }
        }

        return ans;
};