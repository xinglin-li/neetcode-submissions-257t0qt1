class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        # Note that the number are from 1 to 26, not start from 0
        res = []
        while columnNumber:
            columnNumber -= 1
            res.append(chr(columnNumber % 26 + ord("A")))
            columnNumber //= 26
        return "".join(reversed(res))