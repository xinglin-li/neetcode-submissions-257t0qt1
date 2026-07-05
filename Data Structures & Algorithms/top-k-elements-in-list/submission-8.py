class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        for x, c in freq.items():
            buckets[c].append(x)
        ans = []
        for c in range(len(nums), 0, -1):
            for x in buckets[c]:
                ans.append(x)
                if len(ans) == k:
                    return ans