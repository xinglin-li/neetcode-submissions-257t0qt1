class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        prefix = 0
        ans = 0
        freq[0] = 1    
        for num in nums:
            prefix += num
            need = prefix - k
            ans += freq[need]
            freq[prefix] += 1
        return ans
