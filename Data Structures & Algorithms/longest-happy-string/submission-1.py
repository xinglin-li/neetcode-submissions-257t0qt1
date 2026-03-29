class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        h = []
        for cnt,c in  [(a, 'a'), (b, 'b'), (c, 'c')]:
            if cnt > 0:
                heapq.heappush(h,(-cnt,c))
        res = []
        while h:
            cnt1, c1 = heapq.heappop(h)
            if len(res) >= 2 and res[-1] == res[-2] == c1:
                if not h:
                    break
                cnt2, c2 = heapq.heappop(h)
                res.append(c2)
                if cnt2 < -1:
                    cnt2 += 1
                    heapq.heappush(h, (cnt2,c2))
                heapq.heappush(h, (cnt1,c1))
            else:
                res.append(c1)
                if cnt1 < -1:
                    cnt1 += 1
                    heapq.heappush(h, (cnt1, c1))
        return "".join(res)