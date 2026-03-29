class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0

"""
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #Top-down DP solution. O(n^2), O(n)
        desired_idx = len(nums) - 1
        canReach = [False]*len(nums)
        canReach[-1] = True
        for i in range(desired_idx-1,-1,-1):
            step = nums[i]
            for j in range(1, min(step,desired_idx-i)+1):
                if canReach[i+j] == True:
                    canReach[i] = True
        return canReach[0]
"""