class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        
        count_t = Counter(t)
        count = {}
        required = len(count_t)
        formed = 0
        l, r = 0, 0
        min_len = float("inf")
        min_window = ""
        
        while r < len(s):
            char = s[r]
            count[char] = count.get(char, 0) + 1
            
            if char in count_t and count[char] == count_t[char]:
                formed += 1
            
            while l <= r and formed == required:
                char = s[l]
                
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    min_window = s[l:r+1]
                
                count[char] -= 1
                if char in count_t and count[char] < count_t[char]:
                    formed -= 1
                
                l += 1
            
            r += 1
        
        return min_window
                
            