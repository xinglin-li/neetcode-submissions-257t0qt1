class Solution:
    def reorganizeString(self, s: str) -> str:
        cnt = Counter(s)

        # 如果最大频率超过 ceiling(n/2)，必然无法重排
        if max(cnt.values()) > (len(s) + 1) // 2:
            return ""

        # 使用最大堆（Python heapq 是最小堆，所以 push 负数）
        h = [(-v, c) for c, v in cnt.items()]
        heapq.heapify(h)

        res = []

        while len(h) >= 2:
            # 取出频率最高的两个
            v1, c1 = heapq.heappop(h)
            v2, c2 = heapq.heappop(h)

            res.append(c1)
            res.append(c2)

            # 放回堆，频率 -1
            if v1 + 1 < 0:
                heapq.heappush(h, (v1 + 1, c1))
            if v2 + 1 < 0:
                heapq.heappush(h, (v2 + 1, c2))

        # 如果还剩一个字符，说明 freq == 1
        if h:
            res.append(h[0][1])

        return "".join(res)