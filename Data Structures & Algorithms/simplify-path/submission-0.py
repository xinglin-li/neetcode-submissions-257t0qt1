class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        for token in path.split("/"):   
            if token == "" or token == ".":
                # 空的（因为 '//'）或 '.' → 跳过
                continue
            elif token == "..":
                # 返回上一级目录 → 栈非空时弹出
                if stack:
                    stack.pop()
            else:
                # 普通目录名称 → 入栈
                stack.append(token)

        # 拼接成绝对路径
        return "/" + "/".join(stack)