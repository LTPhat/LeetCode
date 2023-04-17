# Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

 

# Example 1:

# Input: s = "bcabc"
# Output: "abc"
# Example 2:

# Input: s = "cbacdcbc"
# Output: "acdb"

class Solution():
    def removeDuplicateLetters(self,s):
        mydict = dict()
        stack = []
        for i in s:
            mydict[i] = mydict.get(i,0) + 1
        for i in s:
            if i in stack:
                mydict[i] -= 1
                continue
            while len(stack) > 0 and stack[-1] > i and mydict[stack[-1]] >= 1:
                stack.pop()
            stack.append(i)
            mydict[i] -= 1
        return ''.join(stack)
def main():
    sol = Solution()
    print(sol.removeDuplicateLetters("bcdbc"))
    print(sol.removeDuplicateLetters("cbacdcbc"))
main()