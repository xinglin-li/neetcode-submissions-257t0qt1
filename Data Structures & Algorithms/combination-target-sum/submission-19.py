class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        path = []
        res = []

        def dfs(i, cumsum):
            if cumsum == target:
                res.append(path[:])
                return
            for j in range(i, n):
                if cumsum + nums[j] > target:
                    continue
                path.append(nums[j])
                dfs(j, cumsum + nums[j])
                path.pop()
        dfs(0, 0)
        return res