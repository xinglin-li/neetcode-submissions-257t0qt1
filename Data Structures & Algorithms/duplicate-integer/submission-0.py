class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count_dict = {}
        for item in nums:
            if item not in count_dict:
                count_dict[item] = 1
            else:
                return True
        return False