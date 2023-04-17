# A valid IP address consists of exactly four integers separated by single dots. Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.

# For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.
# Given a string s containing only digits, return all possible valid IP addresses that can be formed by inserting dots into s. You are not allowed to reorder or remove any digits in s. You may return the valid IP addresses in any order.

 

# Example 1:

# Input: s = "25525511135"
# Output: ["255.255.11.135","255.255.111.35"]
# Example 2:

# Input: s = "0000"
# Output: ["0.0.0.0"]
# Example 3:

# Input: s = "101023"
# Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]



# Algorithm: Backtracking


# State is defined as the position i in s we are currently visiting and the address we have previously build.
# If i == len(s), we have reached to the end of s, and no more state can be generated. We check if the current address we build is of exactly four numbers, and add it to the result if it is.
# Now, at each position i, we have at most two choices, and we need to check for each option to see if it will result in a valid address.
# (1) Add the current digit to the last number in address if the last number is not 0 (No leading zero) and the concatenated number is <= 255.
# (2) Add the current digit in address as a new number if address contains less than 4 numbers.

class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        def backtrack(i, address):
            if i == len(s):
                if len(address) == 4:
                    res.append(".".join(map(str, address)))
                return 
            # (1)    
            if address[-1] != 0 and (10*address[-1] + int(s[i]) <=255):
                last = address[-1]
                address[-1] = 10*last + int(s[i])
                backtrack(i+1, address)
                address[-1] = last
            # (2)
            if len(address) < 4:
                address.append(int(s[i]))
                backtrack(i+1, address)
                address.pop()
        backtrack(1, [int(s[0])])
        return res