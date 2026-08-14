class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []

        def dfs(i, curr_sum):
            if curr_sum == target:
                res.append(path[:])
                return
            if curr_sum > target:
                return
            
            for j in range(i, len(nums)):
                path.append(nums[j])
                dfs(j, curr_sum + nums[j])
                path.pop()

        dfs(0,0)
        return res