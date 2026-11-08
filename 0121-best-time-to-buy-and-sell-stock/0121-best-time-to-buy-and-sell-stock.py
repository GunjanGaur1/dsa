class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        mini = float('inf')
        maxiprofit = 0

        n = len(prices)
        for i in range(n):
            mini=min(mini,prices[i])
            profit = prices[i]-mini
            maxiprofit = max(profit,maxiprofit)
        return maxiprofit