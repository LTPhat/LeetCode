// You are given an array of words where each word consists of lowercase English letters.

// wordA is a predecessor of wordB if and only if we can insert exactly one letter anywhere in wordA without changing the order of the other characters to make it equal to wordB.

// For example, "abc" is a predecessor of "abac", while "cba" is not a predecessor of "bcad".
// A word chain is a sequence of words [word1, word2, ..., wordk] with k >= 1, where word1 is a predecessor of word2, word2 is a predecessor of word3, and so on. A single word is trivially a word chain with k == 1.

// Return the length of the longest possible word chain with words chosen from the given list of words.

 

// Example 1:

// Input: words = ["a","b","ba","bca","bda","bdca"]
// Output: 4
// Explanation: One of the longest word chains is ["a","ba","bda","bdca"].
// Example 2:

// Input: words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
// Output: 5
// Explanation: All the words can be put in a word chain ["xb", "xbc", "cxbc", "pcxbc", "pcxbcf"].
// Example 3:

// Input: words = ["abcd","dbqca"]
// Output: 1
// Explanation: The trivial word chain ["abcd"] is one of the longest word chains.
// ["abcd","dbqca"] is not a valid word chain because the ordering of the letters is changed.
 

// Constraints:

// 1 <= words.length <= 1000
// 1 <= words[i].length <= 16
// words[i] only consists of lowercase English letters.


//                                 bcda
//                         bcd     bda    bca   cda
//                     bd  cd  bd   
//                    b  d c d b d
// 
/**
 * @param {string[]} words
 * @return {number}
 */
var longestStrChain = function(words) {
    let word_visited = {}
    let length_chain_dict = {}
    function get_length_chain(word){
        if (!word_visited[word]) return 0 
        if (length_chain_dict[word]) return length_chain_dict[word]
        let length_chain  = 1
        for (let i = 0; i < word.length; i++){
            sub_word = word.slice(0, i) + word.slice(i+1)
            length_chain = Math.max(length_chain, 1 + get_length_chain(sub_word))
        }
        length_chain_dict[word] = length_chain
        return length_chain
    }
    let max_length_chain = -1
    for (const word of words){
        word_visited[word] = true
    }
    for (const word of words){
        max_length_chain = Math.max(max_length_chain, get_length_chain(word))
    }
    return max_length_chain
};