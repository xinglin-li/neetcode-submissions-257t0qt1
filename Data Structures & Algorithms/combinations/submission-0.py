class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        
        def dfs(i,path):
            if len(path) == k:
                res.append(path.copy())
                return
            for j in range(i,n+1):
                path.append(j)
                dfs(j+1,path)
                path.pop()

        dfs(1,[])
        return res