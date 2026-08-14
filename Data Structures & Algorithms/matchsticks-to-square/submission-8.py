class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total_sum = sum(matchsticks)
        # 正方形 4 条边，总长度必须能被 4 整除
        if total_sum % 4 != 0:
            return False
        
        target = total_sum // 4
        # 关键优化：从大到小排序，优先尝试长火柴，可使无效分支尽早超限剪枝
        matchsticks.sort(reverse=True)
        if matchsticks[0] > target:
            return False
        
        sides = [0] * 4  # 记录正方形 4 条边的当前长度

        def dfs(i):
            if i == len(matchsticks):
                return True
            for j in range(4):
                # 试着将火柴放入第i条边
                if sides[j] + matchsticks[i] <= target:
                    sides[j] += matchsticks[i]
                    if dfs(i + 1):
                        return True
                    sides[j] -= matchsticks[i]
                # 剪枝：如果放置失败且该边长度恰好为 0，说明后续空边效果完全一致，无需重复尝试
                if sides[j] == 0:
                    break
            return False
        return dfs(0) 
        