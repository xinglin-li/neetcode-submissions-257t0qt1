class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # permutation with duplicated
        nums.sort()                # ⭐ 关键1：排序，让相同元素相邻
        res = []
        used = [False] * len(nums) # ⭐ 记录每个位置是否已使用

        def backtrack(path):
            if len(path) == len(nums):
                res.append(path[:])
                return
            
            for i in range(len(nums)):
                if used[i]:
                    continue

                # ⭐⭐ 关键2：去重条件
                # 如果当前元素 == 前一个，并且前一个没有被用过，则跳过！
                # 这是最重要的一行！
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue

                used[i] = True
                path.append(nums[i])
                backtrack(path)
                path.pop()
                used[i] = False

        backtrack([])
        return res

