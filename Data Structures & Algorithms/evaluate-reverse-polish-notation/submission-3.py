class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t not in "+-*/":
                stack.append(int(t))
            else:
                b = stack.pop()  # 注意顺序，先弹出右操作数
                a = stack.pop()  # 再弹出左操作数
                if t == '+':
                    stack.append(a + b)
                elif t == '-':
                    stack.append(a - b)
                elif t == '*':
                    stack.append(a * b)
                elif t == '/':
                    # Python 默认是向下取整（floor），题目要求 toward zero
                    stack.append(int(a / b))
        return stack[0]