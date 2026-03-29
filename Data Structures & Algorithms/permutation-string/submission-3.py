class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # 顺序无关的permutation，可能会用到hash set
        m, n = len(s1), len(s2)
        if m > n:
            return False
        l1 = [0]*26
        l2 = [0]*26
        for i in range(m):
            l1[ord(s1[i]) - ord('a')] += 1
            l2[ord(s2[i]) - ord('a')] += 1
        if l1 == l2:
            return True

        for j in range(m,n):
            l2[ord(s2[j]) - ord('a')] += 1
            l2[ord(s2[j-m]) - ord('a')] -= 1
            if l1 == l2:
                return True
        return False