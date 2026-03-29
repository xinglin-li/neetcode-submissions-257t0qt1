class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        m,n= len(num1), len(num2)
        num1 = num1[::-1]
        num2 = num2[::-1]
        res = [0]*(m+n)
        for i in range(m):
            for j in range(n):
                prod = (ord(num1[i])-48)*(ord(num2[j])-48)
                prod += res[i+j] # Here is the trick
                res[i+j] = prod%10 # Here is the trick, note this is equal sign
                res[i+j+1] += prod//10 # Here is the trick, you don't need to consider carry
        
        while res and res[-1] == 0:
            res.pop()
        
        return "".join([str(i) for i in res[::-1]])