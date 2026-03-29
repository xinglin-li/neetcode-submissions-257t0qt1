class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return 1
        
        up=down=1
        ans=1
        for i in range(1,n):
            if arr[i] > arr[i-1]:
                up = down + 1
                down = 1
                ans = max(ans,up)
            elif arr[i] < arr[i-1]:
                down = up + 1
                up = 1
                ans = max(ans, down)
            else:
                up = down = 1
        return ans