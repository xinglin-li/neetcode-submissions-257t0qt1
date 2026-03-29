class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        res = []
        for i in nums:
            counter[i] = counter.get(i,0) + 1
        z = sorted(list(counter.values()),reverse=True)[:k]
        for k,v in counter.items():
            if v in z:
                res.append(k)
        return res