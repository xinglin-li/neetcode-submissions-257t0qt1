class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # This is actually a tree problem
        nums.sort()
        res, path = [], []

        def dfs(start: int, remain: int):
            if remain == 0:
                res.append(path.copy())
                return
            
            for i in range(start, len(nums)):
                if remain < nums[i]:
                    break
                path.append(nums[i])
                dfs(i, remain - nums[i])
                path.pop()

        dfs(0, target)
        return res
