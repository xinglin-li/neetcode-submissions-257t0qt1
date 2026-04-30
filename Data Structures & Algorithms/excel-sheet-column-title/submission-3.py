class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []
        while columnNumber > 0:
            columnNumber -= 1 # 记住-1. 否则26%26 = 0 -> A, is wrong, we want Z.
            res.append(chr(columnNumber%26 + ord("A")))
            columnNumber //= 26
        return "".join(reversed(res))