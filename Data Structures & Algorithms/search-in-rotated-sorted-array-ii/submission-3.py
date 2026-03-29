class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # Two parts binary search
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            
            # 找到直接返回
            if nums[mid] == target:
                return True

            # 如果左右等于中间 → 无法判断哪边有序，跳过重复数字
            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1
                continue

            # 左半部分有序
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # 右半部分有序
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return False
