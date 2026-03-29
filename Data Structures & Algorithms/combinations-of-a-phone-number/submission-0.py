class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # chars are distinguished
        if not digits:
            return []
        digits_map = {"2":"abc", "3":"def", "4":"ghi",
        "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}

        path = []
        res = []

        def dfs(i):
            if len(path) == len(digits):
                res.append("".join(path))
                return
            if i < len(digits):
                for ch in digits_map[digits[i]]:
                    path.append(ch)
                    dfs(i+1)
                    path.pop()
        
        dfs(0)
        return res

