class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        i = 0
        for j in range(len(nums)):
            if j - i <= k:
                if nums[j] in window:
                    return True
            else:
                window.remove(nums[i])
                i += 1
                if nums[j] in window:
                    return True
            window.add(nums[j])
        return False