class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) < len(b):
            a,b = b,a
        n_b = len(b)
        n_a = len(a)
        a = a[::-1]
        b = b[::-1]
        b = b + "".join(["0" for _ in range(n_a - n_b)])
        carry = 0
        cur_str = ""
        for i in range(n_a):
            num_a = int(a[i])
            num_b = int(b[i])
            cur_sum = num_a + num_b + carry
            if cur_sum == 3:
                cur_str += "1"
                carry = 1
            elif cur_sum == 2:
                cur_str += "0"
                carry = 1
            else:
                cur_str += str(cur_sum)
                carry = 0
        
        if carry == 1:
            cur_str += "1"

        return cur_str[::-1]


