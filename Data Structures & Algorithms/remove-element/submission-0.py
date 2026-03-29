class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        write = 0
        n = len(nums)
        for i in range(n):
            if nums[i] != val:
                nums[write] = nums[i]
                write += 1
        return write