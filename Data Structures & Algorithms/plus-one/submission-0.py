class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] == 9:
            digits[-1] = 0
            carry = 1
        else:
            digits[-1] = digits[-1] + 1
            return digits

        for i in range(len(digits)-2, -1, -1):
            new_digits = (digits[i] + carry)%10
            carry = (digits[i] + carry)//10
            digits[i] = new_digits

        return [1] + digits if carry == 1 else digits 