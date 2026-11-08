class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        mini = float('inf')
        maxiprofit = 0
        n = len(prices)
        profit = 0
        for i in range(1,n):
            if prices[i]>prices[i-1]:
                profit = profit + prices[i]-prices[i-1]
        return profit