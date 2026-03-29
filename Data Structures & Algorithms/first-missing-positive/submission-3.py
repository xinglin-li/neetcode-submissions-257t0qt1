class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # 原地哈希（cyclic sort）
        n = len(nums)

        # Step 1: 把每个正数放到它正确的位置
        # 如果 nums[i] = x 且 1 ≤ x ≤ n
        # 那么它应该在 index x-1
        i = 0
        while i < n:
            x = nums[i]
            # 条件：x 在合法范围 + 不在正确坑里 + Avoid infinite loop when duplicates
            if 1 <= x <= n and nums[x - 1] != x:
                nums[i], nums[x - 1] = nums[x - 1], nums[i]
            else:
                i += 1

        # Step 2: 找第一个 nums[i] != i + 1 的位置
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        # 所有 1..n 都齐了 → 答案是 n+1
        return n + 1
        
