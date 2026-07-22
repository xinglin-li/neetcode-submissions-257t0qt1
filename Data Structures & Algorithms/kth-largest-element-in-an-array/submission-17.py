class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import random
        target_idx = len(nums) - k
        left, right = 0, len(nums) - 1

        while left <= right:
            pivot_idx = random.randint(left, right)
            nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]

            pivot = nums[right]
            i = left
            for j in range(left, right):
                if nums[j] <= pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[i], nums[right] = nums[right], nums[i]

            if i == target_idx:
                return nums[i]
            elif i < target_idx:
                left = i + 1
            else:
                right = i - 1
        
        return -1