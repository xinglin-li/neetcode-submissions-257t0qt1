class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # The key is that you need to be aware with the variant of backtracking problems
        # If the elements are not distinct, then you need to sort the list first
        # Then, for each level, eliminate duplicated elements
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