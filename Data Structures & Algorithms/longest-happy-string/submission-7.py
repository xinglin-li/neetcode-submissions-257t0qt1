class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # 1. 将数量大于 0 的字符及其数量存入最大堆（Python 用负数表示最大堆）
        max_heap = []
        for count, char in [(a, 'a'), (b, 'b'), (c, 'c')]:
            if count > 0:
                heapq.heappush(max_heap, (-count, char))
                
        res = []
        
        while max_heap:
            count, char = heapq.heappop(max_heap)
            
            # 如果结果数组最后两个字符与当前数量最多的字符相同，避免凑成连续 3 个
            if len(res) >= 2 and res[-1] == char and res[-2] == char:
                if not max_heap:
                    break  # 没有次多的字符可用了，直接结束
                
                # 弹出次多的字符
                next_count, next_char = heapq.heappop(max_heap)
                res.append(next_char)
                
                # 次多字符数量 -1 后压回堆内
                if next_count + 1 < 0:
                    heapq.heappush(max_heap, (next_count + 1, next_char))
                
                # 把刚刚不能用的最多字符重新压回堆内，下一轮继续尝试
                heapq.heappush(max_heap, (count, char))
            else:
                # 可以安全放置当前数量最多的字符
                res.append(char)
                if count + 1 < 0:
                    heapq.heappush(max_heap, (count + 1, char))
                    
        return "".join(res)
                

