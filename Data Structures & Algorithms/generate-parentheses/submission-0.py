class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # permutation with duplicated variables
        # and constraints
        elements = ["("]*n + [")"]*n
        path = []
        res = []
        used = [False]*len(elements)

        def is_valid(path):
            stack = []
            for element in path:
                if not stack:
                    stack.append(element)
                elif element == ")" and stack[-1] == "(":
                    stack.pop()
                else:
                    stack.append(element)
            return len(stack) == 0

        def dfs(i):
            if len(path) == 2*n and is_valid(path):
                res.append("".join(path))
                return
            prev = None
            for j in range(len(elements)):
                if used[j] or prev == elements[j]: continue
                prev = elements[j]
                used[j] = True
                path.append(elements[j])
                dfs(j)
                path.pop()
                used[j] = False
        
        dfs(0)
        return res