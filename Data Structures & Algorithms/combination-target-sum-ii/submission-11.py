class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # must sort first
        candidates.sort()
        res = []
        path = []

        def dfs(i, total):
            if total == target:
                res.append(path.copy())
            
            for j in range(i, len(candidates)):
                if total + candidates[j] > target:
                    break
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                path.append(candidates[j])
                dfs(j+1, total + candidates[j])
                path.pop()
        dfs(0,0)
        return res
