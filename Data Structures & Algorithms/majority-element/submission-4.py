class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Boyer–Moore
        mode = None
        count = 0
        for num in nums:
            if count == 0:
                mode = num
            count += 1 if num == mode else -1
        return mode