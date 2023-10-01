# Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

 

# Example 1:

# Input: s = "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"
# Example 2:

# Input: s = "God Ding"
# Output: "doG gniD"

# Two pointer
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = ""
        begin = 0
        for i in range(len(s)):
            if s[i] == " ":
                ans += s[begin:i][::-1] + " "
                begin = i+1
        ans += s[begin:][::-1]
        return ans
    


# One-line
class Solution(object):
    def reverseWords(self, s):
        return " ".join(map(lambda x: x[::-1], s.split()))
