class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # 策略就是能用十元找零就先用十元的
        five = 0
        ten = 0

        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                five -= 1
                ten += 1
            else:
                if five and ten:
                    five -= 1
                    ten -= 1
                else:
                    five -= 3
            if five < 0 or ten < 0:
                return False
        
        return True