class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
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
                    if x != min_heap[0]:
                        return False
                    heapq.heappop(min_heap)
        return True