class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Bucket Sort
        from collections import Counter
        count = Counter(nums)
        buckets = [[] for _ in range(len(nums)+1)]
        for num, freq in count.items():
            buckets[freq].append(num)

        res = []    
        for i in range(len(nums), 0 , -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
