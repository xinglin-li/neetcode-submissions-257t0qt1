class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []
        while columnNumber:
            columnNumber -= 1
            res.append(chr(columnNumber % 26 + ord("A")))
            columnNumber //= 26
        return "".join(reversed(res))