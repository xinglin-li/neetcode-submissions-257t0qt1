class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort() # 必须sort
        res = []
        def backtrack(i, path, total):
            if total == target:
                res.append(path.copy()) # 一个马虎的错误是把copy()写成copy
                return
            
            for j in range(i, len(candidates)):
                # 去重
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                # 剪枝
                if total + candidates[j] > target:
                    break
                path.append(candidates[j])
                backtrack(j+1, path, total + candidates[j])
                path.pop()
        backtrack(0, [], 0)
        return res
