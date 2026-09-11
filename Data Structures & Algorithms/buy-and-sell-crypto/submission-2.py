class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        sell = 1
        buy = 0

        while sell < len(prices):
            if prices[sell] > prices[buy]:
                profit = prices[sell] - prices[buy]
                maxP = max(maxP, profit)
            else:
                buy = sell
            sell += 1
        return maxP
