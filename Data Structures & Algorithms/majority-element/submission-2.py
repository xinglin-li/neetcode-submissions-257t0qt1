class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Boyer–Moore
        mode = 0
        count = 0
        for num in nums:
            if count == 0:
                mode = num
                count += 1
            elif num != mode:
                count -= 1
            else:
                count += 1
        return mode