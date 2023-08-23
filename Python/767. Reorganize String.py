# Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

# Return any possible rearrangement of s or return "" if not possible.

 

# Example 1:

# Input: s = "aab"
# Output: "aba"
# Example 2:

# Input: s = "aaab"
# Output: ""
 

# Constraints:

# 1 <= s.length <= 500
# s consists of lowercase English letters.

class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = [0 for i in range(len(s))]
        freMap = {}
        for i in s:
            freMap[i] = freMap.get(i, 0) + 1
        sortedMap = sorted(freMap.items(),reverse = True, key = lambda x: x[1])
        if sortedMap[0][1] > (len(s) + 1)/ 2:
            return ""
        i = 0
        for c, value in sortedMap:
            for j in range(0, value):
                if i >= len(s): 
                    i = 1
                ans[i] = c
                i += 2
        return "".join(ans)