class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        if n < 2:
            return n
        max_len = 1
        left = 0

        def cmp(a, b):
            if a < b: return -1
            if a > b: return 1
            return 0
        
        for right in range(1, n):
            c = cmp(arr[right-1], arr[right])
            if c == 0:
               # 元素相等，窗口重新收缩到当前位置
               left = right 
            elif right == 1 or c * cmp(arr[right-2], arr[right-1]) == 1:
                left = right - 1
            max_len = max(max_len, right - left + 1)
        return max_len