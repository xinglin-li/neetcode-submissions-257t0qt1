class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        candidates.sort()
        def dfs(i, total):
            if total == target:
                res.append(path.copy())
                return
            if total > target:
                return
            prev = None
            for j in range(i, len(candidates)):
                if candidates[j] == prev:
                    continue
                prev = candidates[j]
                path.append(candidates[j])
                dfs(j+1, total + candidates[j])
                path.pop()

        dfs(0,0)
        return res