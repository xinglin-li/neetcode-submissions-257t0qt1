class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        from collections import Counter
        import heapq
        if len(hand)%groupSize != 0:
            return False
        
        cnt = Counter(hand)
        minHeap = list(cnt.keys())
        heapq.heapify(minHeap)

        while minHeap:
            # You cannot pop the first element at the beginning, you only pop it when the cnt of it is zero
            first = minHeap[0]
            for k in range(first, first + groupSize):
                if k not in cnt:
                    return False
                cnt[k] -= 1
                if cnt[k] == 0:
                    if k != minHeap[0]:
                        return False
                    heapq.heappop(minHeap)
        return True

