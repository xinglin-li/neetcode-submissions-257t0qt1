class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        pl = path.split('/')
        for p in pl:
            if p == "" or p == ".":
                continue
            elif stack and p == "..":
                stack.pop()
            else:
                if p != "..":
                    stack.append(p)
        return "/" + "/".join(stack)