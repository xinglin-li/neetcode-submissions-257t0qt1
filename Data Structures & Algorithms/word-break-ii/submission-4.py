class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)
        res = []
        path = []

        def backtrack(i):
            if i == len(s):
                res.append(" ".join(path))
                return
            
            for j in range(i, len(s)):
                word = s[i : j + 1]
                if word in word_set:
                    path.append(word)
                    backtrack(j + 1)
                    path.pop()
        
        backtrack(0)
        return res