class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        from collections import Counter
        if len(hand) % groupSize != 0:
            return False
        count = Counter(hand)
        for x in sorted(count):
            if count[x] > 0:
                freq = count[x]
                for i in range(groupSize):
                    if freq > count[x+i]:
                        return False
                    count[x+i] -= freq
        return True