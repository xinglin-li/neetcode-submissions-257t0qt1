class Solution:
    def jump(self, nums: List[int]) -> int:
        num_jump = 0
        current_end = 0
        farthest = 0
        for i in range(len(nums)-1):
            farthest = max(farthest, i + nums[i])
            if i == current_end:
                num_jump += 1
                current_end = farthest
        return num_jump