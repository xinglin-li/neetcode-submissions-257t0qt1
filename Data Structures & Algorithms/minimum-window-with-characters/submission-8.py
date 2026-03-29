class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = [0] * 128
        window = [0] * 128

        for c in t:
            need[ord(c)] += 1

        l = 0
        have = 0
        needCount = sum(1 for x in need if x > 0)

        res_len = float('inf')
        res = ""

        for r, c in enumerate(s):
            window[ord(c)] += 1
            if need[ord(c)] > 0 and window[ord(c)] == need[ord(c)]:
                have += 1

            while have == needCount:
                if r - l + 1 < res_len:
                    res_len = r - l + 1
                    res = s[l:r+1]

                window[ord(s[l])] -= 1
                if need[ord(s[l])] > 0 and window[ord(s[l])] < need[ord(s[l])]:
                    have -= 1
                l += 1

        return res


