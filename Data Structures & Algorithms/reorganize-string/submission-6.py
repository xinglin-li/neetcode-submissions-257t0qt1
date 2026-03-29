from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)

        # max heap
        heap = [(-freq, char) for char, freq in count.items()]
        heapq.heapify(heap)

        res = []

        while len(heap) >= 2:
            freq1, char1 = heapq.heappop(heap)
            freq2, char2 = heapq.heappop(heap)

            res.append(char1)
            res.append(char2)

            if freq1 + 1 < 0:
                heapq.heappush(heap, (freq1 + 1, char1))
            if freq2 + 1 < 0:
                heapq.heappush(heap, (freq2 + 1, char2))

        # 处理最后一个
        if heap:
            freq, char = heap[0]
            if -freq > 1:
                return ""
            res.append(char)

        return "".join(res)