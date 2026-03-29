class Solution:
    def isHappy(self, n: int) -> bool:
        # you can use set() to record the loop
        # But use Floyd Cycle Detection is more preferable for a quant
        def next_num(x):
            s = 0
            while x:
                s += (x%10)**2
                x = x//10
            return s
        
        slow = n
        fast = next_num(n)
        while fast != 1 and slow != fast:
            slow = next_num(slow)
            fast = next_num(next_num(fast))
        return fast == 1