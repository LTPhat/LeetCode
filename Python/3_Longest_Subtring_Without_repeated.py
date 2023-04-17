# Given a string s, find the length of the longest substring without repeating characters.

 

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        length = 0
        maxlength = 0
        string = ""
        for i in s:
            if i in string:
                string = string[string.index(i)+1:] + i
            else:
                string += i
                length = len(string)
            maxlength = max(maxlength,length)
        return maxlength
        
def main():
    sol = Solution()
    ans = sol.lengthOfLongestSubstring("abcabcabc")
    print(ans)

main()
