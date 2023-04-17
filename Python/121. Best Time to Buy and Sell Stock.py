# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Example 2:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.
 

# Constraints:

# 1 <= prices.length <= 105
# 0 <= prices[i] <= 104

#Time limited exceed
class Solution(object):
    def maxProfit(self, prices):
        #Using two pointer
        size = len(prices)
        max_profit = 0
        curr_profit = 0
        for i in range (size):
            left = i + 1
            right = size - 1
            while left <= right:
                left_profit = prices[left] - prices[i]
                right_profit = prices[right] - prices[i]
                if left_profit >= right_profit:
                    curr_profit = left_profit
                    max_profit = max(max_profit,curr_profit)
                    right -= 1
                else:
                    curr_profit = right_profit
                    max_profit = max(max_profit,curr_profit)
                    left += 1
        return max_profit 
        
#Time limited exceed               
class Solution(object):
    def maxProfit(self, prices):
        differ = [-90]
        res = []
        i = 0
        while i < len(prices):
            subprice = prices[i]
            for j in range (i + 1,len(prices)):
                differ.append(prices[j] - subprice)
            res.append(max(differ))
            i += 1
        ans = max(res)
        if ans < 0:
            return 0
        return ans
                
        
class Solution(object):
    def maxProfit(self, prices):
        mini = 9999
        max_profit = 0
        for i in range (len(prices)):
            mini = min(mini, prices[i])
            max_profit = max(max_profit, prices[i] - mini)
        return max_profit