class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if not word1:
            return word2
        if not word2:
            return word1
        p1 = 0
        p2 = 0
        res = ""
        while p1 < len(word1) and p2 < len(word2):
            if p1 == p2:
                res += word1[p1]
                p1 += 1
            else:
                res += word2[p2]
                p2 += 1
        if p1 < len(word1):
            return res + word1[p1:]
        if p2 < len(word2):
            return res + word2[p2:]
        return res
