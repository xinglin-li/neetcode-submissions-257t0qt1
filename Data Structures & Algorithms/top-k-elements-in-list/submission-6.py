from collections import Counter

class Solution:
    def topKFrequent(self, nums, k):
        # 1️⃣ 统计频率
        count = Counter(nums)
        
        # 2️⃣ 建桶（频率最多为 len(nums)）
        buckets = [[] for _ in range(len(nums) + 1)]
        
        for num, freq in count.items():
            buckets[freq].append(num)
        
        # 3️⃣ 从高频往低频取
        res = []
        for freq in range(len(buckets) - 1, 0, -1):
            for num in buckets[freq]:
                res.append(num)
                if len(res) == k:
                    return res