class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        counter1 = Counter(s)
        counter2 = Counter(t)
        return counter1 == counter2