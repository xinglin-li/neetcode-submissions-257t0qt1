class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        from functools import cache
        wordSet = set(wordDict)

        @cache
        def dfs(start):
            if start == len(s):
                return [""]
            res = []
            for end in range(start, len(s)):
                word = s[start: end + 1]
                if word in wordSet:
                    sub_sentence = dfs(end + 1)
                    for sub in sub_sentence:
                        sentence = word + (" " + sub if sub else "")
                        res.append(sentence)
            return res
        return dfs(0)

