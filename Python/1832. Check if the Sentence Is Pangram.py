# A pangram is a sentence where every letter of the English alphabet appears at least once.

# Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

 

# Example 1:

# Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
# Output: true
# Explanation: sentence contains at least one of every letter of the English alphabet.
# Example 2:

# Input: sentence = "leetcode"
# Output: false
 

# Constraints:

# 1 <= sentence.length <= 1000
# sentence consists of lowercase English letters.

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        list_dict = {}
        n = len(sentence)
        for i in sentence:
            list_dict[i] = list_dict.get(i,0) + 1
        if len(list_dict) == 26:
            return True
        return False