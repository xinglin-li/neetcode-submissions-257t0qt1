class Solution:
    def isHappy(self, n: int) -> bool:
        # 快慢指针（弗洛伊德循环检测)
        def get_next(number):
            total_sum = 0
            while number > 0:
                number, digit = divmod(number, 10)
                total_sum += digit ** 2
            return total_sum
        
        slow = n
        fast = get_next(n)

        while fast != 1 and slow != fast:
            slow = get_next(slow)
            fast = get_next(get_next(fast))
        
        return fast == 1