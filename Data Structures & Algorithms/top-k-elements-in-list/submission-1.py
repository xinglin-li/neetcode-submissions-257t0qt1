class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            count[num] = count.get(num, 0) + 1
        for num, cnt in count.items():
            freq[cnt].append(num)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res

        """
        counter = Counter(nums)
        return [num for num, _ in counter.most_common(k)]

        """

        """
        counter = {}
        res = []
        for i in nums:
            counter[i] = counter.get(i,0) + 1
        z = sorted(list(counter.values()),reverse=True)[:k]
        for k,v in counter.items():
            if v in z:
                res.append(k)
        return res
        """