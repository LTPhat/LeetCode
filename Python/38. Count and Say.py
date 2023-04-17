# The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

# countAndSay(1) = "1"
# countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.
# To determine how you "say" a digit string, split it into the minimal number of substrings such that each substring contains exactly one unique digit. Then for each substring, say the number of digits, then say the digit. Finally, concatenate every said digit.

# For example, the saying and conversion for digit string "3322251":


# Given a positive integer n, return the nth term of the count-and-say sequence.

 

# Example 1:

# Input: n = 1
# Output: "1"
# Explanation: This is the base case.
# Example 2:

# Input: n = 4
# Output: "1211"
# Explanation:
# countAndSay(1) = "1"
# countAndSay(2) = say "1" = one 1 = "11"
# countAndSay(3) = say "11" = two 1's = "21"
# countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"
 

# Constraints:

# 1 <= n <= 30



class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        #Base case
        if n == 1:
            return "1"
        pre_res = self.countAndSay(n-1)
        res = ""
        char_conse = 1 # To count repeated char in pre_res
        for i in range(len(pre_res)):
            if i == len(pre_res)-1 or pre_res[i] != pre_res[i+1]:
                res += str(char_conse) + pre_res[i]
                char_conse = 1
            else: 
                char_conse += 1
        return res
                