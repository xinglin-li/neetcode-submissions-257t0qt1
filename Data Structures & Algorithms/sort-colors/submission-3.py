class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # Dutch National Flag
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        This is a limited-domain sorting problem (only 0/1/2).
        Because the values are from a small fixed set, we do not need a comparison sort.
        We can solve it in O(n) using counting or the Dutch National Flag algorithm.
        """
        low, mid, high = 0, 0, len(nums) - 1
        while mid <= high:
            if nums[mid] == 0:
                nums[mid] , nums[low] = nums[low], nums[mid]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]

                high -= 1
        return nums