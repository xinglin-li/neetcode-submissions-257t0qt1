class Solution:

    def encode(self, strs: List[str]) -> str:
        return ''.join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            # 先找到分隔符 #
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])          # 取出字符串长度
            res.append(s[j+1:j+1+length]) # 截取真实字符串
            i = j + 1 + length            # 移动指针
        return res
