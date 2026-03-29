class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False
        target = total//k
        buckets = [0]*k
        nums.sort(reverse=True) # Key optimization

        def dfs(i):
            if i == len(nums):
                return True
            for j in range(k):
                if nums[i] + buckets[j] > target:
                    continue
                buckets[j] += nums[i]
                if dfs(i+1):
                    return True
                buckets[j] -= nums[i]
                # Key truncate
                if buckets[j] == 0:
                    break
            return False
        return dfs(0)
                
                