class Solution:
    def isValid(self, s: str) -> bool:
        pop_mapping = {")": "(", "]":"[", "}":"{"}
        stack = []
        for i in s:
            if i in pop_mapping:
                top = stack.pop() if stack else "#"
                if top != pop_mapping[i]:
                    return False
            else:
                stack.append(i)
        return True if not stack else False