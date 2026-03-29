class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) == 1:
            return s

        # expand around center
        def expand(l,r):
            while l >= 0 and r <= len(s)-1 and s[l] == s[r]: 
                l -= 1
                r += 1
            return l+1,r-1
        
        l=r=0
        for i in range(len(s)):
            l1,r1 = expand(i,i)
            if r1 - l1 > r-l:
                l,r=l1,r1
            l2,r2 = expand(i,i+1)
            if r2 - l2 > r-l:
                l,r=l2,r2
        return s[l:r+1]

