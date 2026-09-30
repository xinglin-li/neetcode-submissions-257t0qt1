class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        path = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(i):
            if len(path) == len(digits):
                res.append("".join(path))
                return
            for c in digitToChar[digits[i]]: # there are len(digits) number of trees
                path.append(c)
                backtrack(i + 1)
                path.pop()

        if digits:
            backtrack(0)
        return res
