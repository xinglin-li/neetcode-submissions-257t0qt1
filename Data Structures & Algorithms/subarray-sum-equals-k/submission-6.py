class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        ans = 0
        prefix = 0
        freq[0] = 1

        for x in nums:
            prefix += x
            # prefix - need = k
            need = prefix - k
            ans += freq[need]
            freq[prefix] += 1
        
        return ans