# # Given a string s, partition s such that every 
# # substring
# #  of the partition is a 
# # palindrome
# # . Return all possible palindrome partitioning of s.

 

# # Example 1:

# # Input: s = "aab"
# # Output: [["a","a","b"],["aa","b"]]
# # Example 2:

# # Input: s = "a"
# # Output: [["a"]]


# #Algorithm: Backtracking

# # Consider a function palindrome to check whether a string is palindrome or not.
# # an other function dfs to backtrack with parameters 'i' -> current position and curr -> current solution
# # first condition if postion 'i' is the last position of the string we got our complete traversal and append to the solution
# # else traverse the string from 'i' to len(s) and if current partition 'sol' is palindrome backtrack again for all possible solutions.
# # In a nutshell we get all the possible solutions just by backtracking.

# Ex1: s = "aab"

# a
# a
# b
# appended
# [['a', 'a', 'b']]
# ab
# aa
# b
# appended
# [['a', 'a', 'b'], ['aa', 'b']]
# aab


class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        def check_palindrome(string):
            return string == string[::-1]
        def backtrack(i, curr):
            if i == len(s):
               res.append(curr)
               return 
            for j in range(i, len(s)):
                to_check = s[i:j+1]
                if check_palindrome(to_check):
                    backtrack(j+1, curr+[s[i:j+1]])
            return
        backtrack(0, [])
        return res
