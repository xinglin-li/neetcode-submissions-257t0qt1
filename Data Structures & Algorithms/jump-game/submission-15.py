class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0

        for i, jump in enumerate(nums):
            if i > farthest:
                return False
            farthest = max(i + jump, farthest)
        
        return True

