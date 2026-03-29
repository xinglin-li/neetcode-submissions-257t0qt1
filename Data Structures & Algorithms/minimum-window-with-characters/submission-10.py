from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        need = Counter(t)
        window = defaultdict(int)

        required = len(need)   # 需要满足的“不同字符”种类数
        formed = 0             # 当前窗口已满足 need 的种类数

        # ans: (window_len, left, right)
        ans = (float("inf"), 0, 0)

        l = 0
        for r, ch in enumerate(s):
            window[ch] += 1

            # 如果这个字符的频次刚好满足 need
            if ch in need and window[ch] == need[ch]:
                formed += 1

            # 当窗口已经覆盖 t，开始收缩
            while formed == required and l <= r:
                if (r - l + 1) < ans[0]:
                    ans = (r - l + 1, l, r)

                left_ch = s[l]
                window[left_ch] -= 1

                # 如果移除后，某个必须字符不再满足 need，窗口失效
                if left_ch in need and window[left_ch] < need[left_ch]:
                    formed -= 1

                l += 1

        return "" if ans[0] == float("inf") else s[ans[1]: ans[2] + 1]