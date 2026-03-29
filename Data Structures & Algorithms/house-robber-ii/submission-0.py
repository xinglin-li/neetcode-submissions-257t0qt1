class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 3:
            return max(nums)
        max_include_first = 0
        max_include_last = 0
        a,b = nums[0], max(nums[0],nums[1])
        for i in range(2,n-1):
            a,b = b, max(b,a+nums[i])
        max_include_first = b
        a,b = nums[1], max(nums[1],nums[2])
        for j in range(3,n):
            a,b = b, max(b,a+nums[j])
        max_include_last = b

        return max(max_include_first,max_include_last)
