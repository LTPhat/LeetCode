# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

# Example 1:

# Input: s = "leetcode"
# Output: 0
# Example 2:

# Input: s = "loveleetcode"
# Output: 2
# Example 3:

# Input: s = "aabb"
# Output: -1
class Solution(object):
    def firstUniqChar(self, s):
        mydict = dict()
        for i in s:
            if i in mydict:
                mydict[i] += 1
            else:
                mydict[i] = 1
        for i in range (len(s)):
            if mydict[s[i]] == 1:
                return i
        return -1
def main():
    sol = Solution()
    print(sol.firstUniqChar('leetcode'))
main()