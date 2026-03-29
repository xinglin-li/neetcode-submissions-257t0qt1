class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def backtrack(i):
            # 每到一个节点都要 append 当前 subset
            #res.append(subset[:])
            res.append(subset.copy())
            # 从 i 开始，让每个元素都作为“起点”
            for j in range(i, len(nums)):
                subset.append(nums[j])   # 选择
                backtrack(j + 1)        # 递归
                subset.pop()            # 撤销选择

        backtrack(0)
        return res