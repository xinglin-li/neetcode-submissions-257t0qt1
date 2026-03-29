class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        path = []
        def dfs(i, total):
            if total == target:
                res.append(path.copy())
                return
            
            if total > target:
                return

            for j in range(i, len(nums)):
                path.append(nums[j])
                dfs(j, total + nums[j]) # 关键：dfs(j) → 可以重复使用 nums[j]
                path.pop()
        dfs(0,0)
        return res

"""
# template: subsets. Order is not considered.
def subsets(nums):
    res = []
    subset = []
    def dfs(i):
        res.append(subset.copy())
        for j in range(i, len(nums)):
            subset.append(nums[j])
            dfs(j+1)
            subset.pop()
    dfs(0)
    return res
"""
"""
# template: combinations, combinations of k elements or sum = target
def combine(n, k):
    res = []
    path = []

    def dfs(start):
        if len(path) == k:
            res.append(path.copy())
            return
        
        for num in range(start, n+1):
            path.append(num)
            dfs(num + 1)
            path.pop()

    dfs(1)
    return res

def dfs(i, curr_sum):
    if curr_sum == target:
        res.append(path.copy())
    if curr_sum > target: return

    for j in range(i, len(nums)):
        path.append(nums[j])
        dfs(j, curr_sum + nums[j])   # 可重复选：用 j
        path.pop()
"""
"""
# Permutaion. Order is important, need to maintain visited array. Loop the entire array.
def permute(nums):
    res = []
    used = [False]*len(nums)
    path = []

    def dfs():
        if len(path) == len(nums):
            res.append(path.copy())
            return
        
        for i in range(len(nums)):
            if used[i]: continue
            used[i] = True
            path.append(nums[i])
            dfs()
            path.pop()
            used[i] = False
    dfs()
    return res
"""