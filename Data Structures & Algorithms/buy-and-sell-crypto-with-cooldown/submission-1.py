class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # hold: (1) t-1 is hold. (2) t-1 is rest, and buy at t
        # sold: (1) t-1 is hold.
        # rest: (1) t-1 is sold. (2) t-1 is rest
        hold = -prices[0]
        sold = float("-inf")
        rest = 0
        for price in prices:
            prev_hold = hold
            prev_sold = sold
            prev_rest = rest
            hold = max(prev_hold, prev_rest - price)
            sold = prev_hold + price
            rest = max(prev_rest, prev_sold)
        return max(rest, sold)