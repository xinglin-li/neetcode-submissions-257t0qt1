class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        """
        up[i] 为以 arr[i] 结尾且最后一步是上升（arr[i-1] < arr[i]）的最长湍流长度；
        down[i] 为以 arr[i] 结尾且最后一步是下降（arr[i-1] > arr[i]）的最长湍流长度。
        """
        up = down = 1
        max_len = 1

        for i in range(1, len(arr)):
            if arr[i] > arr[i-1]:
                up = down + 1
                down = 1
            elif arr[i] < arr[i-1]:
                down = up + 1
                up = 1
            else:
                up = down = 1
            max_len = max(max_len, up, down)
        
        return max_len
