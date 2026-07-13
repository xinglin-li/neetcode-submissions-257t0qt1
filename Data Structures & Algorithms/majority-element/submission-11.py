class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Boyer–Moore
        mode = None
        count = 0
        for x in nums:
            if count == 0:
                mode = x
            count += 1 if mode == x else -1     
        return mode