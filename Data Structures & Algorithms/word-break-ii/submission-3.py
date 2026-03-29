class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # 它是一个 DAG + DP 问题
        wordSet = set(wordDict)
        memo = {}
        def dfs(start):
            # return all sentences from index "start".
            if start == len(s):
                return [""]
            if start in memo:
                return memo[start]     
            res = []
            for end in range(start+1, len(s)+1):
                word = s[start:end]
                if word in wordSet:
                    sub_sentences = dfs(end)
                    for sub in sub_sentences:
                        if sub:
                            res.append(word + " " + sub)
                        else:
                            res.append(word)
            memo[start] = res
            return res
        return dfs(0)