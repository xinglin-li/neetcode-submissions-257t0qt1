class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Euler Path, 一笔画问题. Hierholzer算法. 其实就是图的后序遍历. 一笔画走到底, 然后把走过的路径压回去. 先走到底的先入队. 所以最后要reverse.
        graph = defaultdict(list)
        for src, dst in sorted(tickets, reverse = True):
            graph[src].append(dst)

        res = []

        def dfs(node):
            while graph[node]:
                nxt = graph[node].pop()
                dfs(nxt)
            res.append(node)

        dfs("JFK")
        return res[::-1]