class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        max_length = 1
        word_set = set()
        l = 0
        for i in range(len(s)):
            while l < i and s[i] in word_set:
                word_set.remove(s[l])
                l += 1
            max_length = max(max_length, i-l+1)
            word_set.add(s[i])
        return max_length