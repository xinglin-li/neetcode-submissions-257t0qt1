class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # 如果没有trust记录，n必须是1才能成为judge
        if not trust:
            return 1 if n == 1 else -1
        
        # indegree - outdegree
        score = [0] * (n + 1)
        
        for a, b in trust:
            score[a] -= 1   # a trusts someone → 不可能是judge
            score[b] += 1   # b is trusted by someone
        
        # judge 的分数必须是 n-1
        for i in range(1, n + 1):
            if score[i] == n - 1:
                return i
        
        return -1