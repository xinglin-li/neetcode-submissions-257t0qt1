class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Floyd’s Tortoise and Hare: cycle detection
        # Phase 1: Find intersection point of two runners
        slow = nums[0]
        fast = nums[nums[0]]
        
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        # Phase 2: Find the entrance of the cycle
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow