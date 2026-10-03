class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # really good question, which combine hash map and jump game
        # We want the last index for a ch
        last = {}
        for i, x in enumerate(s):
            last[x] = i

        start = end = 0
        res = []
        for i, x in enumerate(s):
            end = max(end, last[x])
            if i == end:
                res.append(end - start + 1)
                start = end + 1
        return res


                






