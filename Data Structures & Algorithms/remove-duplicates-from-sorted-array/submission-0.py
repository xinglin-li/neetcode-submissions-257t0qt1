class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = right = 0
        pos = 0
        while right < len(nums):
            if nums[left] == nums[right] and right - left == 1:
                pos = right
                right += 1
            elif nums[left] == nums[right]:
                right += 1
            elif nums[left] < nums[right] and left < pos:
                nums[pos] = nums[right]
                left += 1
                pos += 1
            else:
                left += 1
                right += 1

        return left+1


