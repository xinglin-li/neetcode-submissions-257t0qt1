class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        # 从最低位（最右侧）开始向前遍历
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits  # 无需进一步进位，直接返回结果
            digits[i] = 0  # 9 + 1 = 10，当前位置 0，继续向高位进位

        # 若循环结束仍未返回，说明所有位都是 9（如 999 -> 1000），需要在头部补 1
        return [1] + digits