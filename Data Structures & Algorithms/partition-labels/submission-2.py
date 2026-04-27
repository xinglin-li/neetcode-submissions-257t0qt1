class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # really good question, which combine hash map and jump game
        # We want the last index for a ch
        last = {c:i for i, c in enumerate(s)}
        begin = 0
        farthest = 0
        end = 0
        res = [] 
        for i in range(len(s)):
            farthest = max(farthest, last[s[i]])
            end = farthest
            if i == farthest:
                res.append(end-begin+1)
                begin = end+1
        return res






