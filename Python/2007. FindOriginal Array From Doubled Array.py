# An integer array original is transformed into a doubled array changed by appending twice the value of every element in original, and then randomly shuffling the resulting array.

# Given an array changed, return original if changed is a doubled array. If changed is not a doubled array, return an empty array. The elements in original may be returned in any order.

 

# Example 1:

# Input: changed = [1,3,4,2,6,8]
# Output: [1,3,4]
# Explanation: One possible original array could be [1,3,4]:
# - Twice the value of 1 is 1 * 2 = 2.
# - Twice the value of 3 is 3 * 2 = 6.
# - Twice the value of 4 is 4 * 2 = 8.
# Other original arrays could be [4,3,1] or [3,1,4].
# Example 2:

# Input: changed = [6,3,0,1]
# Output: []
# Explanation: changed is not a doubled array.
# Example 3:

# Input: changed = [1]
# Output: []
# Explanation: changed is not a doubled array.
from collections import Counter
class Solution(object):
    def findOriginalArray(self, changed):
        """
        :type changed: List[int]
        :rtype: List[int]
        """
        # Len(changed) % 2 != 0
        if len(changed) % 2 != 0:
            return []
        unpaired = Counter()
        original_arr = [] # Ans arr
        changed.sort(reverse = True) #Sort descendently
        for i, num in enumerate(changed):
            if num != 0:
                if 2 * num in unpaired and unpaired[2*num] > 0:
                    unpaired[2*num] -= 1
                    original_arr.append(num)
                elif num % 2 == 0:
                    unpaired[num] += 1
                else: 
                    return []
            else:
                unpaired[num] += 1
        if unpaired[0] % 2 == 0:
            original_arr += [0] * (unpaired[0]//2)
            unpaired [0] = 0
        if all(count == 0 for count in unpaired.values()):
            return original_arr
        else:
            return []
        