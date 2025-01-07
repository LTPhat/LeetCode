# Given an array of string words, return all strings in words that is a substring of another word. You can return the answer in any order.

# A substring is a contiguous sequence of characters within a string

 

# Example 1:

# Input: words = ["mass","as","hero","superhero"]
# Output: ["as","hero"]
# Explanation: "as" is substring of "mass" and "hero" is substring of "superhero".
# ["hero","as"] is also a valid answer.
# Example 2:

# Input: words = ["leetcode","et","code"]
# Output: ["et","code"]
# Explanation: "et", "code" are substring of "leetcode".
# Example 3:

# Input: words = ["blue","green","bu"]
# Output: []
# Explanation: No string of words is substring of another string.


class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        n = len(words)
        ans = []
        # for i in range(0, n):
        #     for j in range(0, n):
        #         if i == j or words[i] in ans:
        #             continue
        #         if words[j].find(words[i]) != -1:
        #             ans.append(words[i])
        
        # return ans
        arr=" ".join(words)
        print(arr)
        subStr=[word for word in words if arr.count(word)>=2]
        return subStr
