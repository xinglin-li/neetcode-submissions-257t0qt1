class Solution:
    def tribonacci(self, n: int) -> int:
        memo = [-1]*(n+1)
        def dfs(i):
            if i == 0:
                return 0
            elif i <= 2:
                return 1
            if memo[i] != -1:
                return memo[i]
            memo[i] = dfs(i-1) + dfs(i-2) + dfs(i-3)
            return memo[i]
        return dfs(n) 
            