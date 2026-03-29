class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        path = []
        def dfs(i):
            res.append(path.copy())
            prev = None
            for j in range(i,len(nums)):
                if nums[j] == prev: continue
                prev = nums[j]
                path.append(nums[j])
                dfs(j+1)
                path.pop()
        dfs(0)
        return res