class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        max_p = 0
        for r in range(len(prices)):
            max_p = max(prices[r]-prices[l],max_p)
            if prices[r] < prices[l]:
                l = r
        return max_p
