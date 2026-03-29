class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # This array is already sorted, so you can use the method below.
        if not nums:
            return 0
        
        slow = 0
        for fast in range(1, len(nums)):
            if nums[slow] != nums[fast]:
                slow += 1
                nums[slow] = nums[fast]
        return slow + 1



