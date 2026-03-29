class Solution:
    def hammingWeight(self, n: int) -> int:
        # Bit Manipulation (Brian Kernighan’s Algorithm)
        count = 0
        while n:
            n &= n - 1
            count += 1
        return count



"""
class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count("1")
"""