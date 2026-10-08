class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        i = 0
        max_profit = 0
        min_price = float('inf')
        n = len(prices)

        for i in range(n):
            min_price = min(min_price,prices[i])
            profit = prices[i]-min_price
            max_profit = max(profit,max_profit)

        return max_profit
            
