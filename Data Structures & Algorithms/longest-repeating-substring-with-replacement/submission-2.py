class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # trick: 寻找并维持一个“包含历史最大重复字符数”的窗口
        count = defaultdict(int)
        left = 0
        max_freq = 0
        ans = 0

        for right, ch in enumerate(s):
            count[ch] += 1
            max_freq = max(max_freq, count[ch])

            while (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1
            
            ans = max(ans, right - left + 1)

        return ans