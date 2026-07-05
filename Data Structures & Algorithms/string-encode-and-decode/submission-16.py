class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = []
        for s in strs:
            ans.append(str(len(s)))
            ans.append("#")
            ans.append(s)
        return "".join(ans)

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            start = j + 1
            ans.append(s[start: start + length])
            i = start + length
        return ans
