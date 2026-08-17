class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        # 基础打家劫舍辅助函数（线性 DP）
        def rob(gain):
            prev1, prev2 = 0, 0
            ans = 0
            for x in gain:
                ans = max(prev2 + x, prev1)
                prev2 = prev1
                prev1 = ans
            return ans
        # 首尾相连转化为两个子问题：不偷首家 nums[1:] 或 不偷尾家 nums[:-1]
        return max(rob(nums[1:]), rob(nums[:-1]))

