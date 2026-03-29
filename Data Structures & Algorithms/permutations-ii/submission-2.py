class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)
        used = [False]*n
        path = []
        def dfs():
            if len(path) == n:
                res.append(path.copy())
                return
            
            for i in range(n):
                if used[i]:
                    continue
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue
                path.append(nums[i])
                used[i] = True
                dfs()
                used[i] = False
                path.pop()
        dfs()
        return res
