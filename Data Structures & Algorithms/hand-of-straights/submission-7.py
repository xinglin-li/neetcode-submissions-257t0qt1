class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        from collections import Counter
        cnt = Counter(hand)
        minHeap = sorted(cnt.keys())
        for x in minHeap:
            while cnt[x] > 0:
                freq = cnt[x]
                for i in range(groupSize):
                    if freq > cnt[x+i]:
                        return False
                    cnt[x+i] -= freq
        return True