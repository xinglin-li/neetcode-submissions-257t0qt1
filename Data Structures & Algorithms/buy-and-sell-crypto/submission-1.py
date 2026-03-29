class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize variables
        min_price = float('inf')  # Minimum price seen so far
        max_profit = 0  # Maximum profit
        
        # Iterate through the prices
        for price in prices:
            # Update the minimum price
            min_price = min(min_price, price)
            # Calculate the profit if sold at the current price
            profit = price - min_price
            # Update the maximum profit
            max_profit = max(max_profit, profit)
        
        return max_profit