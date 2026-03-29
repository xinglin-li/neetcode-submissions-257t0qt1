class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        from collections import defaultdict
        graph = defaultdict(list)
        for from_i, to_i in tickets:
            heapq.heappush(graph[from_i], to_i)
        res = []
        def dfs(node):
            while graph[node]:
                nxt = heapq.heappop(graph[node])
                dfs(nxt)
            res.append(node)
        dfs('JFK')
        return res[::-1]
        
