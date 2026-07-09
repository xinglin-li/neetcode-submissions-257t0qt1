class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)

        if m > n:
            return False

        need = [0] * 26
        window = [0] * 26

        for ch in s1:
            need[ord(ch) - ord("a")] += 1
        
        left = 0

        for right, ch in enumerate(s2):
            window[ord(ch) - ord("a")] += 1
            if right - left + 1 > m:
                window[ord(s2[left]) - ord("a")] -= 1
                left += 1
            if right - left + 1 == m and need == window:
                return True
            
        return False
