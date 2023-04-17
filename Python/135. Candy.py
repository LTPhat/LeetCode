# There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

# You are giving candies to these children subjected to the following requirements:

# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.
# Return the minimum number of candies you need to have to distribute the candies to the children.

 

# Example 1:

# Input: ratings = [1,0,2]
# Output: 5
# Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
# Example 2:

# Input: ratings = [1,2,2]
# Output: 4
# Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
# The third child gets 1 candy because it satisfies the above two conditions.
 

# Constraints:

# n == ratings.length
# 1 <= n <= 2 * 104
# 0 <= ratings[i] <= 2 * 104

class Solution(object):
    def candy(self, ratings):
        size = len(ratings)
        relative_to_left = [1 for i in range(size)] 
        #Make sure that each right neighbor child of ratings[i] has more candy than ratings[i]
        relative_to_right = [1 for i in range(size)]
        #Make sure that each left neighbor child of ratings[i] has more candy than ratings[i]
        for i in range(1, size):
            if ratings[i] > ratings[i-1]:
                relative_to_left[i] = relative_to_left[i-1] + 1
        for i in range (size - 1, 0, -1):
            if ratings[i-1] > ratings[i]:
                relative_to_right[i-1] = relative_to_right[i] + 1
        ans = []
        for i in range(0, size):
            ans.append(max(relative_to_left[i],relative_to_right[i]))
        return sum(ans)