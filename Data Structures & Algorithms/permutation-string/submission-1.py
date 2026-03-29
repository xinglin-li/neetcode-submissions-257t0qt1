class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # create a sliding window with len(s1), count the frequency of words
        n,m = len(s1), len(s2)
        if n > m:
            return False
        s1_count = [0]*26
        win_count = [0]*26
        for ch in s1:
            s1_count[ord(ch)-ord('a')] += 1
        for ch in s2[:n]:
            win_count[ord(ch)-ord('a')] += 1
        if s1_count == win_count:
                return True
        for i in range(n,m):
            win_count[ord(s2[i-n])-ord('a')] -= 1
            win_count[ord(s2[i])-ord('a')] += 1
            if s1_count == win_count:
                return True
        return False
