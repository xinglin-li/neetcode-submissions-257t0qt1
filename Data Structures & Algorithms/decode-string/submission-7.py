class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current_chars = []
        current_number = 0

        for char in s:
            if char.isdigit():
                current_number = current_number*10 + int(char)
            
            elif char == "[":
                stack.append((current_chars, current_number))
                current_chars = []
                current_number = 0
            elif char == "]":
                prev_chars, repeat_count = stack.pop()
                current_chars = prev_chars + current_chars*repeat_count
            else:
                current_chars.append(char)
        
        return "".join(current_chars)