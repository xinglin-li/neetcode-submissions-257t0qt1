class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        write = 0
        n = len(nums)
        for read in range(n):
            if nums[read] != val:
                nums[write] = nums[read]
                write += 1
        return write