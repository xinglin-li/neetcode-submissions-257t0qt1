class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        indeg = defaultdict(int)
        outdeg = defaultdict(int)
        for outdeg_i , indeg_i in trust:
            indeg[indeg_i] += 1
            outdeg[outdeg_i] += 1
        for k,v in indeg.items():
            if v == n-1 and outdeg[k] == 0:
                return k
        return -1