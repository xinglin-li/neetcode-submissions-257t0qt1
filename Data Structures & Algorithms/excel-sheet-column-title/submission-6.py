class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []
        while columnNumber > 0:
            # 类似26进制转换, 但由于字符是从1开始对齐 (1对应'A'), 先减去1移除偏移量
            columnNumber -= 1

            # 取余得到当前最低位的字符 (0->'A', 25->'Z')
            res.append(chr(ord('A') + columnNumber % 26))

            # 除以26进入更高一位的计算
            columnNumber //= 26
        return "".join(reversed(res))