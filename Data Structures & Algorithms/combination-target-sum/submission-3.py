class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()                  # helps pruning; not required by problem
        res, path = [], []

        def dfs(start: int, remain: int):
            if remain == 0:                # found a valid combination
                res.append(path.copy())
                return
            for i in range(start, len(nums)):
                x = nums[i]
                if x > remain:             # further numbers are larger (sorted) -> prune
                    break
                path.append(x)             # choose x
                dfs(i, remain - x)         # i (not i+1) because reuse allowed
                path.pop()                 # undo

        dfs(0, target)
        return res
