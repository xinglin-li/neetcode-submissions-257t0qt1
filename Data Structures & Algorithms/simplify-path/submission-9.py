class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        list_strings = path.split("/")
        for component in list_strings:
            if component == "" or component == ".":
                continue
            if component == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(component)
        return "/"+ "/".join(stack)