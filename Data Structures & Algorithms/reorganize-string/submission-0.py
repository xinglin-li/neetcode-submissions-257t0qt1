class Solution:
    def reorganizeString(self, s: str) -> str:
        cnt = Counter(s)
        n = len(s)
        if max(cnt.values()) > (n+1)//2:
            return ""
        heap = [(-v,k) for k,v in cnt.items()]
        res = []
        heapq.heapify(heap)
        while len(heap)>=2:
            v1, k1 = heapq.heappop(heap)
            v2, k2 = heapq.heappop(heap)

            res.append(k1)
            res.append(k2)
            if v1 < -1:
                v1 += 1
                heapq.heappush(heap,(v1,k1))
            if v2 < -1:
                v2 += 1
                heapq.heappush(heap,(v2,k2))
        if heap:
            res.append(heap[0][1])
        
        return "".join(res)