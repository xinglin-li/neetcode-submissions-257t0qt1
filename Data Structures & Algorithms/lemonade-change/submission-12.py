class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # 策略就是能用十元找零就先用十元的
        five = ten = 0
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if not five:
                    return False
                five -= 1
                ten += 1
            else:  # bill == 20
                # 贪心：优先用 10 + 5 找零，保留更多 5 元备用
                if ten and five:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True