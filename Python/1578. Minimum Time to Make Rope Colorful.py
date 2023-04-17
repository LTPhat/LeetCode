# # Alice has n balloons arranged on a rope. You are given a 0-indexed string colors where colors[i] is the color of the ith balloon.

# # Alice wants the rope to be colorful. She does not want two consecutive balloons to be of the same color, so she asks Bob for help. Bob can remove some balloons from the rope to make it colorful. You are given a 0-indexed integer array neededTime where neededTime[i] is the time (in seconds) that Bob needs to remove the ith balloon from the rope.

# # Return the minimum time Bob needs to make the rope colorful.


# Example 1:


# Input: colors = "abaac", neededTime = [1,2,3,4,5]
# Output: 3
# Explanation: In the above image, 'a' is blue, 'b' is red, and 'c' is green.
# Bob can remove the blue balloon at index 2. This takes 3 seconds.
# There are no longer two consecutive balloons of the same color. Total time = 3.
# Example 2:


# Input: colors = "abc", neededTime = [1,2,3]
# Output: 0
# Explanation: The rope is already colorful. Bob does not need to remove any balloons from the rope.
# Example 3:


# Input: colors = "aabaa", neededTime = [1,2,3,4,1]
# Output: 2
# Explanation: Bob will remove the ballons at indices 0 and 4. Each ballon takes 1 second to remove.
# There are no longer two consecutive balloons of the same color. Total time = 1 + 1 = 2.
 

# Constraints:

# n == colors.length == neededTime.length
# 1 <= n <= 105
# 1 <= neededTime[i] <= 104
# colors contains only lowercase English letters.


class Solution(object):
    def minCost(self, colors, neededTime):
        """
        :type colors: str
        :type neededTime: List[int]
        :rtype: int
        """
        conse_char = 1 #Save number of repeated chars
        max
        running_sum = neededTime[0] #Save sum of needtime for consecutive repeated chars
        max_time = neededTime[0] # Max needtime to reduce through iteration
        total = 0 # Ans: Sum of needtime to remove
        
        for i in range(1, len(colors)):
            if colors[i] == colors[i-1]:
                conse_char += 1 
                running_sum += neededTime[i]
                max_time = max(max_time, neededTime[i])
            else: #not repeated
                if conse_char > 1:      # Process all previous repeated chars
                    total += (running_sum-max_time) #Remove all larger neededTime of an repeated char
                conse_char = 1
                running_sum = neededTime[i] # Continue finding repeated char
                max_time = neededTime[i]
        if conse_char > 1:   #Process the last char
            total += (running_sum - max_time)
        return total