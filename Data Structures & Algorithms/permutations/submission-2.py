class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        used = [False]*len(nums)

        def dfs():
            if len(path) == len(nums):
                res.append(path.copy())
                return
            for j in range(len(nums)):
                if not used[j]:
                    used[j] = True
                    path.append(nums[j])
                    dfs()
                    path.pop()
                    used[j] = False
        dfs()
        return res