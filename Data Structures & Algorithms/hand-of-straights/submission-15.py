class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # 每次都必须从当前最小的牌开始组成连续 groupSize 张。
        # 因为当前最小牌不可能被更小的牌带走，所以它只能作为某个顺子的第一张。
        if len(hand) % groupSize != 0:
            return False
        
        count = Counter(hand)
        min_heap = list(count.keys())
        heapq.heapify(min_heap)

        while min_heap:
            start = min_heap[0]

            for x in range(start, start + groupSize):
                if x not in count:
                    return False
                
                count[x] -= 1

                if count[x] == 0:
                    # 如果不在堆顶, 则堆顶元素无法连成groupSize的连续递增序列
                    if x != min_heap[0]:
                        return False
                    heapq.heappop(min_heap)
        return True
                    
