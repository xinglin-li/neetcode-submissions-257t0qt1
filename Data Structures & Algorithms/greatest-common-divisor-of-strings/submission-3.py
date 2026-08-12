class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # 核心规律：若 str1 和 str2 存在公共因子串，则按照不同顺序拼接必须相等
        if str1 + str2 != str2 + str1:
            return ""
        
        # 若拼接相等，最大公共因子串的长度就是两字符串长度的最大公约数 (GCD)
        max_len = math.gcd(len(str1), len(str2))

        return str1[:max_len]