class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits)-1, -1, -1):
            new_val = digits[i] + carry
            digits[i] = new_val % 10
            carry = new_val // 10
            if carry == 0:
                return digits
        return [1] + digits 