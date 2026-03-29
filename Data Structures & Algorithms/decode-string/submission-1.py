class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for ch in s:
            if ch == ']':
                seq = '' 
                while stack[-1] != "[":
                    seq = stack.pop() + seq
                stack.pop()
                multipier = ""
                while stack and len(stack[-1]) == 1 and ord(stack[-1]) - ord("9") <= 9:
                    multipier = stack.pop() + multipier
                seq *= int(multipier)
                stack.append(seq)
            else:
                stack.append(ch)
        return "".join(stack)