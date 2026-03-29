class Solution:
    def myPow(self, x: float, n: int) -> float:
        # n = b₀ * 2⁰ + b₁ * 2¹ + b₂ * 2² + … + b_k * 2ᵏ
        # x^n = x^{(b₀·2⁰)} · x^{(b₁·2¹)} · x^{(b₂·2²)} … 
        # Binary Exponentiation
        if n == 0:
            return 1.0
        
        if x == 0:
            return 0.0

        # Handle negative exponent
        if n < 0:
            x = 1 / x
            n = -n
        
        res = 1.0
        
        while n > 0:
            # If current bit = 1, multiply x
            if n & 1:
                res *= x
            
            # square x for next bit
            x *= x
            n >>= 1
        
        return res

