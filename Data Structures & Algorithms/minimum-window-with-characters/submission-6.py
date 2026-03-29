class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        count_t = Counter(t)
        required = len(count_t)
        count = {}
        l = 0

        formed = 0
        min_len = float("inf")
        min_win = ""

        for r in range(len(s)):
            char = s[r]
            count[char] = count.get(char, 0) + 1
            if char in count_t and count[char] == count_t[char]:
                formed += 1
            
            while l <= r and formed == required:
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    min_win = s[l: r+1]
                
                char = s[l]
                count[char] -= 1
                if char in count_t and count[char] < count_t[char]:
                    formed -= 1
                l += 1
        return min_win
                

                
            