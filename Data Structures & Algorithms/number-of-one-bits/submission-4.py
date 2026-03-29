
"""
class Solution:
    def hammingWeight(self, n: int) -> int:
        # Bit Manipulation (Brian Kernighan’s Algorithm)
        count = 0
        while n:
            n &= n - 1 # flip the least-significant 1 bit to 0
            count += 1
        return count
"""
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            if n % 2 == 1:
                count += 1
            n >>= 1
        return count
"""
class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count("1")
"""