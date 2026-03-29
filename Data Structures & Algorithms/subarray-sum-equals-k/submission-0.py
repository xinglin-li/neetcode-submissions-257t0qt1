class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # An extension of two sum
        count = 0
        prefix = 0
        prefix_count = {0:1}
        for num in nums:
            prefix += num
            if prefix - k in prefix_count:
                count += prefix_count[prefix - k]
            prefix_count[prefix] = prefix_count.get(prefix,0) + 1
        return count