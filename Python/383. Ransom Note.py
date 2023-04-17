# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.

 

# Example 1:

# Input: ransomNote = "a", magazine = "b"
# Output: false
# Example 2:

# Input: ransomNote = "aa", magazine = "ab"
# Output: false
# Example 3:

# Input: ransomNote = "aa", magazine = "aab"
# Output: true
 

# Constraints:

# 1 <= ransomNote.length, magazine.length <= 105
# ransomNote and magazine consist of lowercase English letter


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        mydict = {}
        for i in magazine:
            mydict[i] = mydict.get(i,0) + 1
        for j in ransomNote:
            if j in mydict:
                if mydict[j] == 1:
                    mydict.pop(j)
                else:
                    mydict[j] -= 1
            else:
                return False
        return True