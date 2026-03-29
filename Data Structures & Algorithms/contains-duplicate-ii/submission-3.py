class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        for i, x in enumerate(nums):
            if len(window) > k:
                window.remove(nums[i-k-1])
            if x in window:
                return True
            window.add(x)
        return False
