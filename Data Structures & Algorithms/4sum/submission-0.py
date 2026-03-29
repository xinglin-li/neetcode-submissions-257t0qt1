class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # 剪枝
            if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target:
                break
            if nums[i] + nums[n-1] + nums[n-2] + nums[n-3] < target:
                continue

            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                
                # 剪枝
                if nums[i] + nums[j] + nums[j+1] + nums[j+2] > target:
                    break
                if nums[i] + nums[j] + nums[n-1] + nums[n-2] < target:
                    continue

                # ⭐ 调用 twoSum()
                two_sum_target = target - nums[i] - nums[j]
                pairs = self.twoSum(nums, j + 1, two_sum_target)

                for l, r in pairs:
                    res.append([nums[i], nums[j], nums[l], nums[r]])

        return res


    # ⭐ 抽出来的 twoSum(双指针)
    # 返回的是索引对 (l, r)
    def twoSum(self, nums, start, target):
        res = []
        l, r = start, len(nums) - 1
        
        while l < r:
            s = nums[l] + nums[r]
            if s == target:
                res.append((l, r))
                l += 1
                while l < r and nums[l] == nums[l - 1]:
                    l += 1
            elif s < target:
                l += 1
            else:
                r -= 1
        return res       