class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        last_val = nums[-1]

        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] > last_val:
                l = mid + 1
            else:
                r = mid - 1
        
        return nums[l]
