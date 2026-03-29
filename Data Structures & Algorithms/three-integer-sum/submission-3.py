class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)

        for i in range(n):
            # 1️⃣ 第一个数去重
            if i > 0 and nums[i] == nums[i-1]:
                continue

            # 剪枝：如果当前数 > 0，不可能再等于0
            if nums[i] > 0:
                break

            left, right = i + 1, n - 1

            while left < right:
                s = nums[i] + nums[left] + nums[right]

                if s == 0:
                    res.append([nums[i], nums[left], nums[right]])

                    # 2️⃣ 去重 left
                    while left < right and nums[left] == nums[left+1]:
                        left += 1

                    # 3️⃣ 去重 right
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1

                    left += 1
                    right -= 1

                elif s < 0:
                    left += 1
                else:
                    right -= 1

        return res