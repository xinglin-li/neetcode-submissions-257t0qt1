class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Boyer–Moore
        mode = None
        count = 0
        for num in nums:
            if count == 0:
                mode = num
            if mode == num:
                count += 1
            else:
                count -= 1
        
        return mode