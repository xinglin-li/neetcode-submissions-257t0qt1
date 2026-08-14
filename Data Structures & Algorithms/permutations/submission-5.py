class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        path = []
        used = [False] * n

        def dfs():
            if len(path) == n:
                res.append(path[:])
                return
            for j in range(n):
                if used[j]: continue
                used[j] = True
                path.append(nums[j])
                dfs()
                path.pop()
                used[j] = False
        
        dfs()
        return res
