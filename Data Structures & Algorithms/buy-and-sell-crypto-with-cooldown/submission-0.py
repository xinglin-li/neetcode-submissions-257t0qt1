class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 3 states dp. hold, sold, rest
        # hold[i] = max(hold[i-1], rest[i-1] - prices[i])
        # sold[i] = prices[i] + hold[i-1]
        # rest[i] = max(rest[i-1], sold[i-1])

        n = len(prices)
        if n <= 1:
            return 0
        
        hold = -prices[0]
        sold = 0
        rest = 0
        for i in range(1,n):
            prev_hold = hold
            prev_sold = sold
            prev_rest = rest
            hold = max(prev_hold, prev_rest - prices[i])
            sold = prices[i] + prev_hold
            rest = max(prev_rest, prev_sold)
        return max(sold, rest)
        