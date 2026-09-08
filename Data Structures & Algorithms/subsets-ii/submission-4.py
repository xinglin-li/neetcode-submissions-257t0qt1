class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        path = []
        res = []

        def dfs(i):
            res.append(path[:])
            for j in range(i, n):
                if j > i and nums[j] == nums[j-1]:
                    continue
                path.append(nums[j])
                dfs(j + 1)
                path.pop()
        dfs(0)
        return res
