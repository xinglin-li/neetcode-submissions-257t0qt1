class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(s):
            n = len(s)
            left, right = 0, n-1
            while left < right:
                if s[left] == s[right]:
                    left += 1
                    right -=1
                else:
                    return False
            return True
        
        n = len(s)
        left, right = 0, n-1
        while left < right:
            if s[left] == s[right]:
               left += 1
               right -=1
            else:
                return is_palindrome(s[left+1:right+1]) or is_palindrome(s[left:right])
        return True
