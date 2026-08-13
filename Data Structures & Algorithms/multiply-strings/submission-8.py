class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # 模拟竖式乘法
        if num1 == "0" or num2 == "0":
            return "0"
        m, n = len(num1), len(num2)
        res = [0] * (m + n)

        # 倒序遍历
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                p1, p2 = i + j, i + j + 1  # p1 为高位（进位），p2 为低位
                # 加上 p2 位置原有的留存数值
                total = mul + res[p2]
                res[p2] = total % 10
                res[p1] += total // 10
        
        res = "".join(map(str,res))
        return res.lstrip("0")