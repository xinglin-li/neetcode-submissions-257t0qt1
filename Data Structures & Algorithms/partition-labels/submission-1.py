class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # really good question, which combine hash map and jump game
        # We want the last index for a ch
        last = {ch: i for i, ch in enumerate(s)}
        res = []
        start = 0
        end = 0
        for i, ch in enumerate(s):
            end = max(end, last[ch])
            if i == end:
                res.append(end-start+1)
                start = end + 1
        return res
        




