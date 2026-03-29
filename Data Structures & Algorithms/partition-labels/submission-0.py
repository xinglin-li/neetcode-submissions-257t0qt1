class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}
        # We want the last index for a ch
        for i, ch in enumerate(s):
            last[ch] = i
        
        start = 0
        farthest = 0
        res = []
        for i, ch in enumerate(s):
            farthest = max(farthest, last[ch])
            if i == farthest:
                length = farthest - start + 1
                res.append(length)
                start = farthest + 1
        return res




