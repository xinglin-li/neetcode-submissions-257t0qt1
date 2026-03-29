class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(i, path):
            s = sum(path)
            if s == target:
                res.append(path.copy())

            if s > target:
                return  

            for j in range(i, len(nums)):
                path.append(nums[j])
                backtrack(j, path)
                path.pop()
        
        backtrack(0, [])
        return res