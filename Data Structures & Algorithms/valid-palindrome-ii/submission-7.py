class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPal(i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        n = len(s)
        l,r = 0, n-1
        while l<r:
            if s[l] != s[r]:
                return isPal(l+1,r) or isPal(l,r-1)
            l += 1
            r -=1
        return True
