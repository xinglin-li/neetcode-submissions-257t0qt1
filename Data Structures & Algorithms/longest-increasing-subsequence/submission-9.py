class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = [nums[0]]
        
        for x in nums[1:]:
            if tails and x > tails[-1]:
                tails.append(x)
                continue
            left, right = 0, len(tails)
            while left <= right:
                mid = (left + right) // 2
                if tails[mid] < x:
                    left = mid + 1
                else:
                    right = mid - 1
            tails[left] = x
        
        return len(tails)