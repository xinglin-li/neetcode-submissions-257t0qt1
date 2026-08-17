class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 这道题恶心在indexing
        if not s:
            return ""
        
        start, end = 0, 0
        # 中心扩散法：分别处理奇数长度中心 (i, i) 和偶数长度中心 (i, i+1)
        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # 此时的right和left是越界后的index
            return right - left - 1
        
        for i in range(len(s)):
            len1 = expand(i, i) # 只产生奇数长度回文
            len2 = expand(i, i+1) # 只产生偶数长度回文
            max_len = max(len1, len2)

            if max_len > end - start:
                # 利用 Python 整除 // 对奇偶数向下取整的特性, 统一了indexing
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
        
        return s[start: end + 1]