class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # The key is that you need to maintain a used list
        # Also, you need to search from start each time
        res = []
        path = []
        used = [False]*len(nums)
        def dfs(i):
            if len(path) == len(nums):
                res.append(path.copy())
                return
            for j in range(len(nums)):
                if not used[j]:
                    used[j] = True
                    path.append(nums[j])
                    dfs(j)
                    path.pop()
                    used[j] = False

        dfs(0)
        return res