class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        m, n = len(num1), len(num2)
        res = [0] * (m + n)
        
        num1 = num1[::-1]
        num2 = num2[::-1]
        
        for i in range(m):
            for j in range(n):
                product = (ord(num1[i]) - 48) * (ord(num2[j]) - 48)
                product += res[i + j]
                
                res[i + j] = product % 10
                res[i + j + 1] += product // 10
        
        # 去掉 leading zero
        while len(res) > 1 and res[-1] == 0:
            res.pop()
        
        return ''.join(str(x) for x in res[::-1])
