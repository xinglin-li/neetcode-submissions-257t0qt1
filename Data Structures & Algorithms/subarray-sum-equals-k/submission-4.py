class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        freq[0] = 1
        prefix = 0
        ans = 0
        for x in nums:
            prefix += x
            need = prefix - k
            ans += freq[need]
            freq[prefix] += 1
        return ans