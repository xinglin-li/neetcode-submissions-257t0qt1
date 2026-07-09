class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # In Python, adding strings is much slower than join list of strings
        i, j = 0, 0
        res = []

        while i < len(word1) or j < len(word2):
            if i < len(word1):
                res.append(word1[i])
                i += 1

            if j < len(word2):
                res.append(word2[j])
                j += 1

        return "".join(res)


