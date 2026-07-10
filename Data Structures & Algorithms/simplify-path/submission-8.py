class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for component in path.split("/"):
            if component == "" or component == ".":
                continue
            if component == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(component)
        return "/"+ "/".join(stack)