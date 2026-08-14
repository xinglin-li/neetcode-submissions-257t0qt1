class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        from functools import cache
        word_set = set(wordDict)
        @cache
        def dfs(i):
            if i == len(s):
                return [""]
            res = []
            for j in range(i, len(s)):
                word = s[i:j+1]
                if word in word_set:
                    sub_sentences = dfs(j + 1)
                    for sub in sub_sentences:
                        sentence = (word + " " + sub).strip()
                        res.append(sentence)
            return res
        
        return dfs(0)
            