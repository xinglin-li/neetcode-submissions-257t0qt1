class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        bill_on_hand = defaultdict(int)
        for bill in bills:
            bill_on_hand[bill] += 1
            change = bill - 5
            while change > 0:
                if bill_on_hand[change] > 0:
                    bill_on_hand[change] -= 1
                    change = 0
                elif bill_on_hand[10] > 0 and 10 < change:
                    bill_on_hand[10] -= 1
                    change -= 10
                elif bill_on_hand[5] > 0 and 5 < change:
                    bill_on_hand[5] -= 1
                    change -= 5
                else:
                    break
            if change != 0:
                return False   
        return True       