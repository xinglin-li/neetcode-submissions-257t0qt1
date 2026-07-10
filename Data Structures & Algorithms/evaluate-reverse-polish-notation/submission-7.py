class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {"+", "-", "*", "/"}

        for token in tokens:
            if token not in ops:
                stack.append(int(token))
                continue
            right = stack.pop()
            left = stack.pop()

            if token == "+":
                res = left + right
            elif token == "-":
                res = left - right
            elif token == "*":
                res = left * right
            else:
                res = int(left/right)
            stack.append(res)
        return stack[-1]