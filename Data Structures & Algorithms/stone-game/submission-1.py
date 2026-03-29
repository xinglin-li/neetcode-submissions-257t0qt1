class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # sum_even = piles[0] + piles[2] + ...
        # sum_odd  = piles[1] + piles[3] + ...
        # even number of piles, total sum is odd
        # sum_even !=  sum_odd
        # Alice can choose the larger one
        return True