class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        mini = float('inf')
        maxiprofit = 0
        n = len(prices)
        for i in range(n):
            mini = min(prices[i],mini)
            profit = prices[i]-mini
            maxiprofit = max(maxiprofit,profit)
        return maxiprofit