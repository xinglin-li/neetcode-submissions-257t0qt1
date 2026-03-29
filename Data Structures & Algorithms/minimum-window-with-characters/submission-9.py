from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        target = Counter(t)
        window = defaultdict(int)

        required = len(target)
        formed = 0
        ans = (float("inf"), 0, 0)
        l = 0
        for r in range(len(s)):
            window[s[r]] += 1
            if window[s[r]] == target[s[r]]:
                formed += 1
            while l <= r and formed == required:
                len_win = r - l
                if len_win < ans[0]:
                    ans = (len_win, l, r)
                s_l = s[l]
                l += 1
                window[s_l] -= 1
                if window[s_l] == target[s_l] - 1:
                    formed -=1
        return s[ans[1]: ans[2]+1] if ans[0] != float('inf') else ""