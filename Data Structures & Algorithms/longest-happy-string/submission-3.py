class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        h = []
        for cnt, ch in [(a, 'a'), (b, 'b'), (c, 'c')]:
            if cnt > 0:
                heapq.heappush(h, (-cnt, ch))
        
        res = []
        
        while h:
            cnt1, ch1 = heapq.heappop(h)
            # 尝试放最多的那个
            if len(res) >= 2 and res[-1] == res[-2] == ch1:
                # 不能放三连，必须找第二多的
                if not h:
                    break
                cnt2, ch2 = heapq.heappop(h)
                res.append(ch2)
                cnt2 += 1  # 因为 cnt 是负数
                if cnt2 < 0:
                    heapq.heappush(h, (cnt2, ch2))
                # 把最多的放回去, the most important step!!!
                heapq.heappush(h, (cnt1, ch1))
            else:
                # 可以放 ch1
                res.append(ch1)
                cnt1 += 1
                if cnt1 < 0:
                    heapq.heappush(h, (cnt1, ch1))
        
        return "".join(res)