class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        win = set()
        left = 0
        for right, x in enumerate(nums):
            if x in win:
                return True
            win.add(x)
            if right - left + 1 > k:
                win.remove(nums[left])
                left += 1
        return False