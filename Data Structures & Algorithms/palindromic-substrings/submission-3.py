class Solution:
    def countSubstrings(self, s: str) -> int:
        # 统计以 (left, right) 为中心扩散的回文子串数量
        def expand(l,r):
            count = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # 每扩一次, 相当于多一种回文字
                count += 1
                l -= 1
                r += 1
            return count
        
        ans = 0
        for i in range(len(s)):
            # 累加奇数长度与偶数长度回文串
            ans += expand(i,i)
            ans += expand(i,i+1)

        return ans