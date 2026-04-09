class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            # 最后一个合法的 palindrome 是 (l+1, r-1)
            return s[l+1:r]
        
        for i in range(len(s)):
            s1 = expand(i, i)
            s2 = expand(i, i+1)
            if len(s1) > len(ans):
                ans=s1
            if len(s2) > len(ans):
                ans=s2
            
        return ans
