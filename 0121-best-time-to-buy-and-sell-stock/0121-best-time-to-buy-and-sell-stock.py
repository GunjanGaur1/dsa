class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        maxi = 0
        maxi_profit = 0
        mini = float('inf')
        for i in range(n):
            mini = min(mini,prices[i])
            print(mini)
            maxi_profit = prices[i]-mini
            maxi = max(maxi_profit,maxi)
        return maxi
