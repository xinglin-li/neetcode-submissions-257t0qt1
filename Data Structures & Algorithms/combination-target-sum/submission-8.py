class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        path = []
        def dfs(i, total):
            if total == target:
                res.append(path.copy())
                return
            
            if total > target:
                return

            for j in range(i, len(nums)):
                path.append(nums[j])
                dfs(j, total + nums[j]) # 关键：dfs(j) → 可以重复使用 nums[j]
                path.pop()
        dfs(0,0)
        return res
