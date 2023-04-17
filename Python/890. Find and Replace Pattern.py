# Given a list of strings words and a string pattern, return a list of words[i] that match pattern. You may return the answer in any order.

# A word matches the pattern if there exists a permutation of letters p so that after replacing every letter x in the pattern with p(x), we get the desired word.

# Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter, and no two letters map to the same letter.

 

# Example 1:

# Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
# Output: ["mee","aqq"]
# Explanation: "mee" matches the pattern because there is a permutation {a -> m, b -> e, ...}. 
# "ccc" does not match the pattern because {a -> c, b -> c, ...} is not a permutation, since a and b map to the same letter.
# Example 2:

# Input: words = ["a","b","c"], pattern = "a"
# Output: ["a","b","c"]
 

# Constraints:

# 1 <= pattern.length <= 20
# 1 <= words.length <= 50
# words[i].length == pattern.length
# pattern and words[i] are lowercase English letters.


# Algorithm: Create list of numeric pattern of each string in list words
# ex: words = ["abc","deq","mee","aqq","dkd","ccc"]
# --> l  = [[123],[123],[122],[122],[121],[111]]
# Check numeric pattern of p:
# If numeric pattern of p equals to numeric pattern of words[i], ans.append(words[i])

from collections import defaultdict

class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        def numeric_pattern(w):
            l = []
            m = defaultdict()
            i = 0
            for c in w:
                if c in m:
                    l.append(m[c])
                else:
                    i += 1
                    m[c] = i
                    l.append(m[c])
                return l
        ans = []
        pfind = numeric_pattern(pattern)
        for word in words:
            if numeric_pattern[word] == pfind:
                ans.append(word)
        return ans




