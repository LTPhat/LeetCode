# You are given a 0-indexed array of strings words and a 2D array of integers queries.

# Each query queries[i] = [li, ri] asks us to find the number of strings present in the range li to ri (both inclusive) of words that start and end with a vowel.

# Return an array ans of size queries.length, where ans[i] is the answer to the ith query.

# Note that the vowel letters are 'a', 'e', 'i', 'o', and 'u'.

 

# Example 1:

# Input: words = ["aba","bcb","ece","aa","e"], queries = [[0,2],[1,4],[1,1]]
# Output: [2,3,0]
# Explanation: The strings starting and ending with a vowel are "aba", "ece", "aa" and "e".
# The answer to the query [0,2] is 2 (strings "aba" and "ece").
# to query [1,4] is 3 (strings "ece", "aa", "e").
# to query [1,1] is 0.
# We return [2,3,0].
# Example 2:

# Input: words = ["a","e","i"], queries = [[0,2],[0,1],[2,2]]
# Output: [3,2,1]
# Explanation: Every string satisfies the conditions, so we return [3,2,1].


class Solution(object):
    def vowelStrings(self, words, queries):
        """
        :type words: List[str]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        # Brute Force --> TLE
        # def check_valid(str, wovels):
        #     return str[0] in wovels and str[-1] in wovels

        # wovels = ["a", "e", "i", "o", "u"]
        # ans = [0] * len(queries)
        # for i, (left, right) in enumerate(queries):
        #     count = 0
        #     for j in range(left, right + 1):
        #         if check_valid(words[j], wovels):
        #             count += 1
        #     ans[i] = count

        # return ans

        # Prefix sum
        def check_valid(str, wovels):
            return str[0] in wovels and str[-1] in wovels
            
        vowels = set(["a", "e", "i", "o", "u"])
        prefix_sum = [0] * len(words)
        prefix_sum[0] = 1 if check_valid(words[0], vowels) else 0

        # Create prefix sum
        for i in range(1, len(words)):
           prefix_sum[i] = prefix_sum[i - 1] + (1 if check_valid(words[i], vowels) else 0)

        ans = [0] * len(queries)
        for i, (left, right) in enumerate(queries):
            if left == 0:
                ans[i] = prefix_sum[right]
            else:
                ans[i] = prefix_sum[right] - prefix_sum[max(0, left - 1)]
        
        return ans

        
         
 


