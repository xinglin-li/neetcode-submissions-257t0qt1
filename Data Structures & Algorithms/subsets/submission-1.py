class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset = []
        res = []
        def backtrack(i):
            res.append(subset.copy())
            for j in range(i,len(nums)):
                subset.append(nums[j])
                backtrack(j+1)
                subset.pop()
        backtrack(0)
        return res