class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # two-pointer + in-place replacement.
        # 与 val 相等就跳过, 不相等就覆盖
        write = 0
        for read in nums:
            if read != val:
                nums[write] = read
                write += 1
        return write