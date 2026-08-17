class Solution:
    def jump(self, nums: List[int]) -> int:
        # current_end 是上一个区间的farthest
        jumps = 0
        current_end = 0  # 当前步数能覆盖的最右端
        farthest = 0     # 下一步能覆盖的最远端
        # 遍历到 n - 2 即可，因为在终点前触发最后一次跳跃便能到达终点
        for i in range(len(nums) - 1):
            farthest = max(farthest, nums[i] + i)
            if i == current_end:
                jumps += 1
                current_end = farthest
        return jumps