class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        if total % 4 != 0:
            return False
        target = total // 4
        sides = [0] * 4
        matchsticks.sort(reverse=True) # key optimization

        # we are selecting matchsticks
        def dfs(i):
            if len(matchsticks) == i:
                return True
            
            for j in range(4):
                if sides[j] + matchsticks[i] > target:
                    continue
                
                sides[j] += matchsticks[i]
                if dfs(i + 1):
                    return True
                sides[j] -= matchsticks[i]

                if sides[j] == 0:
                    break
            return False
        
        return dfs(0)