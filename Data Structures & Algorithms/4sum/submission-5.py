class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def twoSum(nums, start, target):
            res = []
            l, r = start, len(nums) - 1
            while l<r:
                s = nums[l] + nums[r]
                if s == target:
                    res.append((l,r))
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                elif s < target:
                    l += 1
                else:
                    r -= 1
            return res
        nums.sort()
        res = []    
        n = len(nums)
        for i in range(n-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, n-2):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                two_sum_target = target - nums[i] - nums[j]
                pairs = twoSum(nums, j + 1, two_sum_target)
                for l,r in pairs:
                    res.append([nums[i], nums[j], nums[l], nums[r]])
        return res
