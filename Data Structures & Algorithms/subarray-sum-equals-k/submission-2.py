class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # An extension of two sum. The tirck is prefix[j] - prefix[i] = sum(nums[i+1:j])
        # prefix[j] - prefix[i] = k -> sum(nums[i+1:j]) = k
        # prefix[j] - k = prefix[i] -> sum(nums[i+1:j]) = k
        # Then, if we know how many prefix[i] == prefix[j] - k, we can figure this question out
        count = 0
        prefix = 0
        seen = {0: 1}  # prefix sum = 0 出现过 1 次（空前缀）
        for x in nums:
            prefix += x
            # 如果 prefix - k 曾经出现过，这些位置开头的 subarray 都可以构成 sum=k
            if prefix - k in seen:
                count += seen[prefix - k]
            # 更新 prefix 出现次数
            seen[prefix] = seen.get(prefix, 0) + 1
        return count