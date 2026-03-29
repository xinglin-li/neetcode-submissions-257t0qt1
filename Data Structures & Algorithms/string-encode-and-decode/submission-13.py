class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}#{s}" for s in strs)
    def decode(self, s: str) -> List[str]:
        res = []
        len_s = len(s)
        i = 0
        while i < len_s:
            j=i
            while s[j] != "#":
                j+=1
            length = int(s[i:j])
            i = j+1+length
            res.append(s[i-length:i])
        return res