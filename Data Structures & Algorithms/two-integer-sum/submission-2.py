class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comp_map = {}
        for i, num in enumerate(nums):
            if num in comp_map:
                return [comp_map[num], i]
            else:
                comp_map[target - num] = i
        
