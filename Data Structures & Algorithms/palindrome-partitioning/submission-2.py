class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []

        def is_pal(left, right):
            while left < right:
                if s[left] == s[right]:
                    left += 1
                    right -= 1
                else:
                    return False
            return True
        
        def dfs(i):
            if len(s) == i:
                res.append(path.copy())
                return
            
            for j in range(i, len(s)):
                if is_pal(i, j):
                    path.append(s[i: j + 1])
                    dfs(j + 1)
                    path.pop()
        
        dfs(0)
        return res
