class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        candidates.sort()
        def dfs(i, total):
            if total == target and path not in res:
                res.append(path.copy())
                return
            if total > target:
                return
            
            for j in range(i, len(candidates)):
                path.append(candidates[j])
                dfs(j+1, total + candidates[j])
                path.pop()

        dfs(0,0)
        return res