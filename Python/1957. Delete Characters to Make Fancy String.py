# A fancy string is a string where no three consecutive characters are equal.

# Given a string s, delete the minimum possible number of characters from s to make it fancy.

# Return the final string after the deletion. It can be shown that the answer will always be unique.

 

# Example 1:

# Input: s = "leeetcode"
# Output: "leetcode"
# Explanation:
# Remove an 'e' from the first group of 'e's to create "leetcode".
# No three consecutive characters are equal, so return "leetcode".
# Example 2:

# Input: s = "aaabaaaa"
# Output: "aabaa"
# Explanation:
# Remove an 'a' from the first group of 'a's to create "aabaaaa".
# Remove two 'a's from the second group of 'a's to create "aabaa".
# No three consecutive characters are equal, so return "aabaa".
# Example 3:

# Input: s = "aab"
# Output: "aab"
# Explanation: No three consecutive characters are equal, so return "aab".

class Solution(object):
    def makeFancyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Sol 1
        # res_string = ""
        # n = len(s)
        # for i in range(0, min(n, 2)):
        #     res_string += s[i]
        # for i in range(2, n):
        #     if s[i] == s[i - 1] and s[i] == s[i - 2]:
        #         continue
        #     res_string += s[i]

        # return res_string 

        # Sol 2
        curr_count, prev_char = 0, None
        list_acc_chars = []
        for char in s:
            if char == prev_char:
                if curr_count < 2:
                    curr_count += 1
                    list_acc_chars.append(char)
            else:
                prev_char = char
                curr_count = 1
                list_acc_chars.append(char)

        return "".join(list_acc_chars)

