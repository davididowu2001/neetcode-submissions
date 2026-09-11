class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        sell = 1
        buy = 0

        while sell < len(prices):
            sell = buy + 1
            while  sell < len(prices) and prices[sell] > prices[buy]:
                profit = prices[sell] - prices[buy]
                maxP = max(maxP, profit)
                sell += 1
            buy +=1
            sell +=1
        return maxP
