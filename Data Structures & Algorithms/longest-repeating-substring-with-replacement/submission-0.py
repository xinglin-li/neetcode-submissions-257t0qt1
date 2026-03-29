class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        max_count = 0
        l = 0
        max_len = 0
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            max_count = max(max_count, count[s[r]])
            while r - l + 1 - max_count > k:
                count[s[l]] -= 1
                l += 1
            max_len = max(max_len, r-l+1)
        return max_len

