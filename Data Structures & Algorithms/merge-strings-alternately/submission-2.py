class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # In Python, adding strings is much slower than join list of strings
        i, j = 0, 0
        res = []
        while i < len(word1) and j < len(word2):
            res.append(word1[i])
            res.append(word2[j])
            i += 1
            j += 1
        res.append(word1[i:])
        res.append(word2[j:])
        return "".join(res)


