class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {
                'I': 1, 'V': 5, 'X': 10, 'L': 50,
                'C': 100, 'D': 500, 'M': 1000
            }
        total = 0
        n = len(s)

        for i in range(n):
            # key: 当前字符代表的数值小于下一个字符, 代表减法规则
            if i < n - 1 and roman_map[s[i]] < roman_map[s[i + 1]]:
                total -= roman_map[s[i]]
            else:
                total += roman_map[s[i]]
        
        return total