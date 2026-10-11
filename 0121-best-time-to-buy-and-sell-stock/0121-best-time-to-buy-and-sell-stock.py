class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        max_profit = 0
        min_price = float('inf')
        for i in range(n):
            min_price = min(min_price,prices[i])
            profit = prices[i] - min_price
            max_profit = max(max_profit,profit)
        return max_profit

