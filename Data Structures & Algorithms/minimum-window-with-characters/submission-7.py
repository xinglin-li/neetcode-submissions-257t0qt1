class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
        len_s, len_t = len(s), len(t)
        if len_s < len_t:
            return ""

        need = Counter(t)
        window = Counter()
        best_len = float("inf")
        res = ""
        have = 0
        need_count = len(need)
        l = 0
        for r, ch in enumerate(s):
            window[ch] += 1
            len_win = l-r+1
            if ch in need and window[ch] == need[ch]:
                have += 1
            
            while have == need_count:
                if r-l+1 < best_len:
                    best_len = r-l+1
                    res = s[l:r+1]
                window[s[l]] -= 1
                if s[l] in need and window[s[l]] < need[s[l]]:
                    have -= 1
                l += 1
        return res


