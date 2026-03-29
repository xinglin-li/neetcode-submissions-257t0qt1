class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        s = sum(nums)
        if s % k != 0:
            return False
        
        target = s // k
        nums.sort(reverse=True)

        buckets = [0] * k
        
        def dfs(i):
            if i == len(nums):
                return all(b == target for b in buckets)
            
            for j in range(k):
                if buckets[j] + nums[i] <= target:
                    buckets[j] += nums[i]
                    if dfs(i + 1):
                        return True
                    buckets[j] -= nums[i]
                
                if buckets[j] == 0:       # 🔥 对称性剪枝：非常重要
                    break
            
            return False
        
        return dfs(0)
