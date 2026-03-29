class Solution:
    def isValid(self, s: str) -> bool:
        pair = {")":"(", "}":"{","]":"["}
        stack = [] 
        for ch in s:
            if ch in pair:
                if not stack or stack[-1] != pair[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)
        return not stack
