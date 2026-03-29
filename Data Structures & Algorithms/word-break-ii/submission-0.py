class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)
        memo = {}

        def dfs(i):
            if i == len(s):
                return [""]      # 返回空句子

            if i in memo:
                return memo[i]

            res = []
            for j in range(i+1, len(s)+1):
                word = s[i:j]
                if word in wordSet:
                    tails = dfs(j)     # tails 是后半句的所有组合
                    for tail in tails:
                        if tail == "":
                            res.append(word)
                        else:
                            res.append(word + " " + tail)

            memo[i] = res
            return res

        return dfs(0)
