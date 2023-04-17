# Given an integer array nums of size n, return the minimum number of moves required to make all array elements equal.

# In one move, you can increment or decrement an element of the array by 1.

# Test cases are designed so that the answer will fit in a 32-bit integer.

 

# Example 1:

# Input: nums = [1,2,3]
# Output: 2
# Explanation:
# Only two moves are needed (remember each move increments or decrements one element):
# [1,2,3]  =>  [2,2,3]  =>  [2,2,2]
# Example 2:

# Input: nums = [1,10,2,9]
# Output: 16

class Solution(object):
    def minMoves2(self, nums):
        nums.sort()
        median = nums[int(len(nums)/2)]
        ans = 0
        for i in range(len(nums)):
            if nums[i] == median:
                continue
            else:
                differ = abs(median-nums[i])
                ans += differ    
        return ans
def main():
    sol = Solution()
    nums =[1,10,2,9]
    print(sol.minMoves2(nums))
main()