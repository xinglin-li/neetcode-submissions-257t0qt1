class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)
        memo = {}

        # dfs(i) return all combination composed by s[i:]
        def dfs(i):
            if i in memo:
                return memo[i]
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
            
            memo[i] = res
            return res
        
        return dfs(0)
            