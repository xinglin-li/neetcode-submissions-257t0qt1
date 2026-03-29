class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        from collections import Counter
        freq = Counter(tasks)
        freq_max = max(freq.values())
        k = sum(1 for val in freq.values() if val == freq_max)
        return max(len(tasks),(freq_max - 1)*(n+1) + k)