class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        temp = numbers[l] + numbers[r]
        while l<r and temp != target:
            if temp < target:
                l += 1
            elif temp > target:
                r -= 1
            temp = numbers[l] + numbers[r]
        return [l+1,r+1]