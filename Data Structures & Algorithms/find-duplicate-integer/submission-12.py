class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow = nums[0]
        # 必须是 while slow != fast. 否则如果一开始, slow就等于fast会出错
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
