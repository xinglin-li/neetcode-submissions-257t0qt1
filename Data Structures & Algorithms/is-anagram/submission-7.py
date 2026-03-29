class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        c1, c2 = Counter(s), Counter(t)
        return c1 == c2