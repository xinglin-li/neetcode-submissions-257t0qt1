class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Another solution, which can unify Jump Game I and II
        farthest = 0
        current_end = 0
        for i in range(len(nums)-1):
            farthest = max(farthest, i + nums[i])
            if i == current_end:
                if current_end == farthest:
                    return False
                current_end = farthest
        return True
