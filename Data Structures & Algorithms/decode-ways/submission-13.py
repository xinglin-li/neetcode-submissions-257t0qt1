class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        next1, next2 = 1, 0

        for i in range(n-1,-1,-1):

            if s[i] == "0":
                cur = 0
            else:
                cur = next1
                if i < n - 1 and (1<=int(s[i:i+2])<=26):
                    cur += next2
            next1, next2 = cur, next1
        return cur



