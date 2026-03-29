class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # permutation with duplicated
        nums.sort()
        path = []
        n = len(nums)
        used = [False]*n
        res = []
        def dfs():
            if len(path) == n:
                res.append(path.copy())
            for i in range(n):
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])
                    dfs()
                    used[i] = False
                    path.pop()
        dfs()
        return res

