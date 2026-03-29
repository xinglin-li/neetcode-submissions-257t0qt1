class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]

        # phase 1
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # phase 2
        slow = nums[0]
        while True:
            if slow == fast:
                break
            slow = nums[slow]
            fast = nums[fast]

        return slow