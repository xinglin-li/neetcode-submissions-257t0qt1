class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        words_set = set()
        length = 1
        l = 0
        for r in range(len(s)):
            while l < r and s[r] in words_set:
                words_set.remove(s[l])
                l += 1
            words_set.add(s[r])
            length = max(length, r-l+1)
        return length

