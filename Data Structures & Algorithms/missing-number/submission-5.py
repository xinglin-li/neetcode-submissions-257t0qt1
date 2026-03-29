class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        if nums[0] != 0:
            return 0
        i=1
        s=0 
        while i<len(nums):
            if nums[i] - s != 1:
                return s + 1
            i += 1
            s += 1
        return s+1