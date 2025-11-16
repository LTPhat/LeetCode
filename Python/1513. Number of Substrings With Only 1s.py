# Given a binary string s, return the number of substrings with all characters 1's. Since the answer may be too large, return it modulo 109 + 7.

 

# Example 1:

# Input: s = "0110111"
# Output: 9
# Explanation: There are 9 substring in total with only 1's characters.
# "1" -> 5 times.
# "11" -> 3 times.
# "111" -> 1 time.
# Example 2:

# Input: s = "101"
# Output: 2
# Explanation: Substring "1" is shown 2 times in s.
# Example 3:

# Input: s = "111111"
# Output: 21
# Explanation: Each substring contains only 1's characters.

class Solution(object):
    def numSub(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        left, right = 0, 0
        count = 0
        MODULE = (10 ** 9  + 7)
        while left < n:
            # Ignore 0's
            if s[left] != '1':
                left += 1
                continue
            # When catch the first '1'
            right = left
            # Get the length of consecutive 1's
            while right < n and s[right] == '1':
                right += 1
            # Calculate number of 1's substrings of found consecutive 1's
            n_1s_seq = right - left 
            count = (count + n_1s_seq * (n_1s_seq + 1) / 2) % MODULE
            # Start finding next 1's
            left = right
    
        return count 