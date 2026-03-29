class Solution:
    def decodeString(self, s: str) -> str:
        num_stack = []
        str_stack = []
        curr_str = ""
        curr_num = 0
        for c in s:
            if c.isdigit():
                curr_num = curr_num*10 + int(c)
            elif c == "[":
                num_stack.append(curr_num)
                str_stack.append(curr_str)
                curr_num = 0
                curr_str = ""
            elif c == "]":
                k = num_stack.pop()
                prev_str = str_stack.pop()
                curr_str = prev_str + curr_str*k
            else:
                curr_str += c
        return curr_str