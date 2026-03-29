class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        s = sum(matchsticks)
        if s % 4 != 0:
            return False
        
        target = s // 4
        matchsticks.sort(reverse=True)      # 🚀 最重要剪枝：从大到小

        # 四条边
        edges = [0] * 4                     

        def dfs(i):
            if i == len(matchsticks):        
                # 所有火柴都放完了
                return edges[0] == edges[1] == edges[2] == edges[3] == target
            
            for k in range(4):              # 试图把第 i 根火柴放到第 k 条边
                if edges[k] + matchsticks[i] <= target:
                    edges[k] += matchsticks[i]
                    if dfs(i + 1):
                        return True
                    edges[k] -= matchsticks[i]

            
            return False

        return dfs(0)
