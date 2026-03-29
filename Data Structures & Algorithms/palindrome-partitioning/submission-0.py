class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # this is a combination
        res = []
        path = []
        def is_palindrome(s):
            l = 0
            r = len(s) - 1
            while l<r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        def dfs(i):
            if len("".join(path)) == len(s):
                res.append(path.copy())
                return

            for j in range(i, len(s)):
                if is_palindrome(s[i:j+1]):
                    path.append(s[i:j+1])
                    dfs(j+1)
                    path.pop()
                else:
                    continue
        dfs(0)
        return res