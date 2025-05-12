# You are given an integer array digits, where each element is a digit. The array may contain duplicates.

# You need to find all the unique integers that follow the given requirements:

# The integer consists of the concatenation of three elements from digits in any arbitrary order.
# The integer does not have leading zeros.
# The integer is even.
# For example, if the given digits were [1, 2, 3], integers 132 and 312 follow the requirements.

# Return a sorted array of the unique integers.

 

# Example 1:

# Input: digits = [2,1,3,0]
# Output: [102,120,130,132,210,230,302,310,312,320]
# Explanation: All the possible integers that follow the requirements are in the output array. 
# Notice that there are no odd integers or integers with leading zeros.
# Example 2:

# Input: digits = [2,2,8,8,2]
# Output: [222,228,282,288,822,828,882]
# Explanation: The same digit can be used as many times as it appears in digits. 
# In this example, the digit 8 is used twice each time in 288, 828, and 882. 
# Example 3:

# Input: digits = [3,7,5]
# Output: []
# Explanation: No even integers can be formed using the given digits.
 

# Constraints:

# 3 <= digits.length <= 100
# 0 <= digits[i] <= 9
from collections import defaultdict

class Solution(object):
    def findEvenNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)
        ans = []
        num_set = set()
        for a in range(n):
            for b in range(n):
                for c in range(n):
                    if digits[a] == 0:
                        continue
                    if a == b or b == c or c == a:
                        continue
                    if digits[c] % 2 != 0:
                        continue
                    num = digits[a] * 100 + digits[b] * 10 + digits[c]
                    num_set.add(num)
        return sorted(list(num_set))






## ============= SOLUTION 2 : HASH TABLE ===================================
        n = len(digits)
        dict_ = defaultdict(int)
        ans = []
        for digit in digits:
            dict_[digit] = dict_.get(digit, 0) + 1
        
        for a in range(1, 10):
            if dict_.get(a, 0) == 0:
                continue
            dict_[a] -= 1
            for b in range(0, 10):
                if dict_.get(b, 0) == 0:
                    continue
                dict_[b] -= 1
                for c in [0, 2, 4, 6, 8]:
                    if dict_.get(c, 0) == 0:
                        continue
                    num = a * 100 + b * 10 + c
                    ans.append(num)
                dict_[b] += 1
            dict_[a] += 1
        
        return ans
