class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        path = []
        res = []
        def dfs(i):
            res.append(path[:])
            for j in range(i, n):
                path.append(nums[j])
                dfs(j+1)
                path.pop()
        dfs(0)
        return res
            