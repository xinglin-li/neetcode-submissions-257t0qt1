class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        words_set = set()
        length = 1
        l = 0
        for i in range(len(s)):
            while l < i and s[i] in words_set:
                words_set.remove(s[l])
                l += 1
            words_set.add(s[i])
            length = max(length, i-l+1)
        return length

