class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # the key issue of this question is that the elements are not distinct
        # you have to sort the candidates first
        # For each level, you skip the elements appeared once.
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