class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        s = sum(nums)
        if s % k: return False
        target = s // k
        subsums = [0]*k
        n = len(nums)
        def dfs(i):
            if i == n:
                for subsum in subsums:
                    if subsum != target:
                        return False
                return True
            
            for j in range(k):
                if nums[i] + subsums[j] <= target:
                    subsums[j] += nums[i]
                    if dfs(i+1):
                        return True
                    subsums[j] -= nums[i]
                if subsums[j] == 0:
                    break
            return False
        
        return dfs(0)
