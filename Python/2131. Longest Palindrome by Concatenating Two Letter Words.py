# You are given an array of strings words. Each element of words consists of two lowercase English letters.

# Create the longest possible palindrome by selecting some elements from words and concatenating them in any order. Each element can be selected at most once.

# Return the length of the longest palindrome that you can create. If it is impossible to create any palindrome, return 0.

# A palindrome is a string that reads the same forward and backward.

 

# Example 1:

# Input: words = ["lc","cl","gg"]
# Output: 6
# Explanation: One longest palindrome is "lc" + "gg" + "cl" = "lcggcl", of length 6.
# Note that "clgglc" is another longest palindrome that can be created.
# Example 2:

# Input: words = ["ab","ty","yt","lc","cl","ab"]
# Output: 8
# Explanation: One longest palindrome is "ty" + "lc" + "cl" + "yt" = "tylcclyt", of length 8.
# Note that "lcyttycl" is another longest palindrome that can be created.
# Example 3:

# Input: words = ["cc","ll","xx"]
# Output: 2
# Explanation: One longest palindrome is "cc", of length 2.
# Note that "ll" is another longest palindrome that can be created, and so is "xx".
 

# Constraints:

# 1 <= words.length <= 105
# words[i].length == 2
# words[i] consists of lowercase English letters.
from collections import Counter

class Solution(object):
    def longestPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        word_counter = Counter(words)
        center_used, total_length = False, 0
        for word in list(word_counter.keys()):
            word_rev = word[::-1]
            # Case 1: Similar pair: 'gg', etc.
            if word_rev == word:
                n_pairs = word_counter[word] // 2
                total_length += n_pairs * 4
                word_counter[word] -= n_pairs * 2
                # Check the last pair and whether the center position is used
                if not center_used and word_counter[word] > 0:
                    center_used = True # Use this last pair at the center position
                    total_length += 2
            # Case 2: Other pairs: 'ab', 'ba'
            else:
                if word_rev in word_counter:
                    n_pairs = min(word_counter[word], word_counter[word_rev]) 
                    total_length += n_pairs * 4
                    word_counter[word] -= n_pairs
                    word_counter[word_rev] -= n_pairs

        
        return total_length
