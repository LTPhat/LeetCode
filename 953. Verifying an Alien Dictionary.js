// In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

// Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographically in this alien language.

 

// Example 1:

// Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
// Output: true
// Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
// Example 2:

// Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
// Output: false
// Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
// Example 3:

// Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
// Output: false
// Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).


// Algorithm: Store index of elements of order in hash-table. 
// Consider every 2 elements in words, check in "valid" function


/**
 * @param {string[]} words
 * @param {string} order
 * @return {boolean}
 */
var isAlienSorted = function(words, order) {
    let indexMap = {};
    // Store index of element in alien order
    for (let i = 0; i < order.length; i++){
        indexMap[order[i]] = i;
    }
    function valid(word1, word2){
        let length = word1.length < word2.length ? word1.length: word2.length;
        for (let i = 0; i < length; i++){
            if (indexMap[word1[i]] > indexMap[word2[i]]){
                return false;
            }
            if(indexMap[word1[i]] < indexMap[word2[i]]){
                return true;
            }
        }
        return word1.length <= word2.length;
    }
    for (let i = 0; i < words.length - 1; i++){
        if (valid(words[i], words[i+1]) == false){
            return false;
        }
    }
    return true;
};