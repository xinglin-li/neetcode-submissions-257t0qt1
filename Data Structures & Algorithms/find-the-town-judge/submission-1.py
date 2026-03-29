class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if not trust:
            return 1 if n == 1 else -1
        
        indeg = defaultdict(int)
        outdeg = defaultdict(int)
        
        for a, b in trust:
            indeg[b] += 1
            outdeg[a] += 1
        
        for k in range(1, n + 1):
            if indeg[k] == n - 1 and outdeg[k] == 0:
                return k
        
        return -1