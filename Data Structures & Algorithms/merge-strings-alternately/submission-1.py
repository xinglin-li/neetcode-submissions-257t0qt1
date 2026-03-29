class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # In Python, adding strings is much slower than join list of strings
        i = j = 0
        res = []
        while i < len(word1) and j < len(word2):
            if i <= j:
                res.append(word1[i])
                i += 1
            else:
                res.append(word2[j])
                j += 1
        s = "".join(res) 
        s += word1[i:]
        s += word2[j:]
        return s


