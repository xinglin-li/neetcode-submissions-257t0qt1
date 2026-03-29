class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = r = 0
        n = len(prices)
        max_profit = 0
        for i in range(1,n):
            r = i
            if prices[i] < prices[l]:
                l = i 
            pf = prices[r] - prices[l]
            max_profit = max(max_profit, pf)
        return max_profit
