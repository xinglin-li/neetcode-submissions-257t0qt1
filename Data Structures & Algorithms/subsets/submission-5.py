class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        def backtrack(i):
            res.append(subset[:])
            for j in range(i,len(nums)):
                subset.append(nums[j])
                backtrack(j+1)
                subset.pop()
        backtrack(0)
        return res