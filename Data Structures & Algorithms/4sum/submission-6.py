class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)

        for i in range(n - 3):
            # 1️⃣ i 去重
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # 剪枝：当前 i 的最小和已经 > target，后面只会更大
            min1 = nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3]
            if min1 > target:
                break

            # 剪枝：当前 i 的最大和仍 < target，说明 i 太小，换下一个 i
            max1 = nums[i] + nums[n - 1] + nums[n - 2] + nums[n - 3]
            if max1 < target:
                continue

            for j in range(i + 1, n - 2):
                # 2️⃣ j 去重
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                # 剪枝：固定 i,j 后最小和 > target
                min2 = nums[i] + nums[j] + nums[j + 1] + nums[j + 2]
                if min2 > target:
                    break

                # 剪枝：固定 i,j 后最大和 < target
                max2 = nums[i] + nums[j] + nums[n - 1] + nums[n - 2]
                if max2 < target:
                    continue

                left, right = j + 1, n - 1
                while left < right:
                    s = nums[i] + nums[j] + nums[left] + nums[right]
                    if s == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])

                        # 3️⃣ left 去重
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        # 4️⃣ right 去重
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1

                        left += 1
                        right -= 1
                    elif s < target:
                        left += 1
                    else:
                        right -= 1

        return res




 