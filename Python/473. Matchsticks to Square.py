# You are given an integer array matchsticks where matchsticks[i] is the length of the ith matchstick. You want to use all the matchsticks to make one square. You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.

# Return true if you can make this square and false otherwise.

 

# Example 1:


# Input: matchsticks = [1,1,2,2,2]
# Output: true
# Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.
# Example 2:

# Input: matchsticks = [3,3,3,3,4]
# Output: false
# Explanation: You cannot find a way to form a square with all the matchsticks.
 

# Constraints:

# 1 <= matchsticks.length <= 15
# 1 <= matchsticks[i] <= 108

#Time limited exceed

class Solution(object):
    def makesquare(self, matchsticks):
        length = sum(matchsticks)//4
        side = [0]*4
        if sum(matchsticks) /4 != length:
            return False
        matchsticks.sort(reverse = True)
        def backtracking(i):
            if i == len(matchsticks):
                return True
            for j in range(4):
                if side[j] + matchsticks[i] <= length:
                    side[j] += matchsticks[i]
                    if backtracking(i+1) == True:
                        return True
                    side[j] -= matchsticks[i]
            return False
        return backtracking(0)

#Accepted
class Solution(object):
    def makesquare(self, matchsticks):
        if sum(matchsticks) %4 != 0:
            return False
    
        target = sum(matchsticks)//4
    
        matchsticks.sort(reverse = True)
    
        ans = [0]*4
    
        def dfs(idx):
            if idx == len(matchsticks):
                return len(set(ans)) == 1
        
            for i in range(4):
                if ans[i] + matchsticks[idx] <= target:
                    ans[i] += matchsticks[idx]
                
                    if dfs(idx+1):
                        return True
                
                    ans[i] -= matchsticks[idx]
                
                    if ans[i] == 0:
                        break
                
            return False
    
        return dfs(0)