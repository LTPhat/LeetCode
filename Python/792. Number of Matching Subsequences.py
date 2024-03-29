# Given a string s and an array of strings words, return the number of words[i] that is a subsequence of s.

# A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

# For example, "ace" is a subsequence of "abcde".
 

# Example 1:

# Input: s = "abcde", words = ["a","bb","acd","ace"]
# Output: 3
# Explanation: There are three strings in words that are a subsequence of s: "a", "acd", "ace".
# Example 2:

# Input: s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
# Output: 2
 

# Constraints:

# 1 <= s.length <= 5 * 104
# 1 <= words.length <= 5000
# 1 <= words[i].length <= 50
# s and words[i] consist of only lowercase English letters.
from collections import defaultdict
class Solution:
    def numMatchingSubseq(self, s, words):
        lookup = defaultdict(list)
        output = 0
        for i,c in enumerate(s):
            lookup[c].append(i)
        def bnr_search(lst,i):
            l,r = 0,len(lst)
            while l<r:
                mid = (l+r)//2
                if i < lst[mid]:
                    r = mid
                else:   
                    l = mid+1
            return l
        for w in words:
            prev = -1
            found = True
            for c in w:
                tmp = bnr_search(lookup[c],prev)
                if tmp == len(lookup[c]):
                    found = False
                    break
                else: 
                    prev = lookup[c][tmp]
            if found:
                output +=1
        return output