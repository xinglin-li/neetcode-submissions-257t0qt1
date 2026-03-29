from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        # dynamically pop maxima.
        count = Counter(s)

        # max heap.
        heap = [(-freq, char) for char, freq in count.items()]
        heapq.heapify(heap)

        if -heap[0][0] > (len(s)+1)//2:
            return ""

        res = []
        while heap and len(heap) >1:
            freq1, c1 = heapq.heappop(heap)
            res.append(c1)
            freq2, c2 = heapq.heappop(heap)
            res.append(c2)
            if freq1 + 1 < 0:
                heapq.heappush(heap, (freq1 + 1, c1))
            if freq2 + 1 < 0:
                heapq.heappush(heap, (freq2 + 1, c2))

        s = "".join(res)
        if heap:
            s = s + (-heap[0][0])*heap[0][1]
        return s