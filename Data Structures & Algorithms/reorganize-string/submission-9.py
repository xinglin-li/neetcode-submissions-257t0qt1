class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = Counter(s)
        max_freq = max(counts.values())

        if max_freq > (len(s) + 1) // 2:
            return ""
        
        max_heap = [(-cnt, char) for char, cnt in counts.items()]
        heapq.heapify(max_heap)

        res = []
        prev_cnt, prev_char = 0, ""

        while max_heap:
            cnt, char = heapq.heappop(max_heap)
            res.append(char)
            cnt += 1

            if prev_cnt < 0:
                heapq.heappush(max_heap, (prev_cnt, prev_char))
            
            prev_cnt = cnt
            prev_char = char
        
        return "".join(res)