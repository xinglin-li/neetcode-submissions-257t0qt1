class Solution:
    def isValid(self, s: str) -> bool:
        pair = {")":"(", "}":"{", "]":"["}
        stack = []

        for ch in s:
            if ch in pair:
                if not stack or pair[ch] != stack[-1]:
                    return False
                stack.pop()
            else:
                stack.append(ch)
        return not stack