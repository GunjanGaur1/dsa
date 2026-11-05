class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        mini = prices[0]
        n = len(prices)
        maxi = 0

        for i in range(n):
            mini = min(mini,prices[i])
            profit = prices[i] -  mini
            maxi = max(profit,maxi)

        return maxi
            

