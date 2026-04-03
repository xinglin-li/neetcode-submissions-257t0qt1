class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Euler Path, 一笔画问题. Hierholzer算法.
        from collections import defaultdict
        graph = defaultdict(list)
        tickets.sort(reverse=True)
        for u,v in tickets:
            graph[u].append(v)
        res = []
        def dfs(node):
            while graph[node]:
                nxt = graph[node].pop()
                dfs(nxt)
            res.append(node)
        dfs("JFK")
        return res[::-1]