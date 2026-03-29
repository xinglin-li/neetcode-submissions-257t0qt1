class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s or len(s) == 1:
            return 1
        n = len(s)
        def expand(l,r):
            count = 0
            while l>=0 and r<=len(s)-1 and s[l] == s[r]:
                l-=1
                r+=1
                count += 1
            return count
        count = 0
        for i in range(n):
            odd_count = expand(i,i)
            even_count = expand(i,i+1)
            count = count + odd_count + even_count
        return count