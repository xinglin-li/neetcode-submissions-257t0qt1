class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memo = {}

        def dfs(i):
            # 站在第 0 阶或第 1 阶上，初始花销都是 0
            if i <= 1:
                return 0
            if i in memo:
                return memo[i]
            res = min(dfs(i - 1) + cost[i - 1], dfs(i - 2) + cost[i - 2])
            memo[i] = res
            return res
        return dfs(n)