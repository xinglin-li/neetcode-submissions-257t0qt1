class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Math: max(len(tasks), (max(freq)-1)*(n+1) + c_max)
        from collections import Counter
        count = Counter(tasks)
        max_freq = max(count.values())
        c_max = 0
        for freq in count.values():
            if freq == max_freq:
                c_max += 1
        return max(len(tasks), (max_freq-1)*(n+1) + c_max)