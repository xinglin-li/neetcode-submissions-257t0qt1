class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 核心：每一天作为卖出日，只需要知道之前最低买入价。
        min_price = float("inf")
        ans = 0
        for price in prices:
            min_price = min(price, min_price)
            ans = max(ans, price - min_price)
        return ans