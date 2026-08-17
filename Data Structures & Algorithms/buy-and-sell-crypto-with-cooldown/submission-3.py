class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # hold: (1) t-1 is hold. (2) t-1 is rest, and buy at t
        # sold: (1) t-1 is hold.
        # rest: (1) t-1 is sold. (2) t-1 is rest
        if not prices:
            return 0
            
        hold = -prices[0]  # 持有股票
        sold = 0           # 当天刚卖出（处于冷冻期）
        rest = 0           # 自由态（未持有且不在冷冻期，随时可买入）
        
        for price in prices[1:]:
            prev_hold = hold
            prev_sold = sold
            
            hold = max(prev_hold, rest - price)  # 保持持有 或 自由态买入
            sold = prev_hold + price            # 卖出股票进入冷冻期
            rest = max(rest, prev_sold)         # 保持自由态 或 冷冻期结束
            
        return max(sold, rest)