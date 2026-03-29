class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        def dfs(path):
            if len(path) == n:
                res.append(path.copy())
                return
            
            for i in range(n):
                if nums[i] not in path:
                    path.append(nums[i])
                    dfs(path)
                    path.pop()
        dfs([])
        return res
