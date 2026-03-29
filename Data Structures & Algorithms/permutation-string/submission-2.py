class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # create a sliding window with len(s1), count the frequency of words
        n, m = len(s1), len(s2)
        if n > m:
            return False

        cnt1 = [0] * 26
        cnt2 = [0] * 26

        for c in s1:
            cnt1[ord(c) - ord('a')] += 1
        for c in s2[:n]:
            cnt2[ord(c) - ord('a')] += 1

        if cnt1 == cnt2:
            return True

        for i in range(n, m):
            cnt2[ord(s2[i]) - ord('a')] += 1
            cnt2[ord(s2[i - n]) - ord('a')] -= 1
            if cnt1 == cnt2:
                return True

        return False
