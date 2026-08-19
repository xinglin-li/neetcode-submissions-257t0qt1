class Solution:
    # 无状态协议编码。格式使用 长度 + '#' + 内容（例如 ["lint","code"] 编码为 "4#lint4#code"）
    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(f"{len(s)}#{s}")
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            # 找到分隔符 '#'
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            # 切片提取原字符串
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return res
