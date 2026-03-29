class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # two-pointer + in-place replacement.
        # 与 val 相等就跳过, 不相等就覆盖
        write = 0
        n = len(nums)
        for read in range(n):
            if nums[read] != val:
                nums[write] = nums[read]
                write += 1
        return write