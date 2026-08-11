class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        max_heap = []
        for count, char in [(a, 'a'), (b, 'b'), (c, 'c')]:
            if count > 0:
                max_heap.append((-count, char))
        heapq.heapify(max_heap)

        res = []
        while max_heap:
            cnt, char = heapq.heappop(max_heap)
            # 判断结果末尾是否会产生3个连续相同字符, 如果是的话, 不能直接用char
            if len(res) >= 2 and res[-1] == char and res[-2] == char:
                if not max_heap:
                    break
                # greedy, 取出频率第二高的字符
                cnt2, char2 = heapq.heappop(max_heap)
                res.append(char2)
                cnt2 += 1
                if cnt2 < 0:
                    heapq.heappush(max_heap, (cnt2, char2))
                # 重新把char压回heap
                heapq.heappush(max_heap, (cnt, char))
            else:
                res.append(char)
                cnt += 1
                if cnt < 0:
                    heapq.heappush(max_heap, (cnt, char))
        return "".join(res)

