class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        path = []
        res = []
        used = [False] * n
        
        def dfs():
            if len(path) == n:
                res.append(path[:])
                return
            
            for i in range(n):
                if used[i]:
                    continue
                used[i] = True
                path.append(nums[i])
                dfs()
                path.pop()
                used[i] = False
        dfs()
        return res