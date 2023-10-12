# Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.

 

# Example 1:

# Input: words = ["bella","label","roller"]
# Output: ["e","l","l"]
# Example 2:

# Input: words = ["cool","lock","cook"]
# Output: ["c","o"]
 

# Constraints:

# 1 <= words.length <= 100
# 1 <= words[i].length <= 100
# words[i] consists of lowercase English letters.



class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        ans = []
        char_freq = {}
        for i, word in enumerate(words):
            for char in word:
                if char not in char_freq:
                    char_freq[char] = [0] * len(words)
                    char_freq[char][i] = 1
                else:
                    char_freq[char][i] += 1

        for char in char_freq.keys():
            for i in range(0, min(char_freq[char])):
                ans.append(char)
            
        return ans
        