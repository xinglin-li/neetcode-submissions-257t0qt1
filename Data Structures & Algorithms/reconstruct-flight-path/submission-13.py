class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for src, dst in sorted(tickets, reverse=True):
            adj[src].append(dst)
        
        route = []

        def dfs(curr):
            while adj[curr]:
                nxt = adj[curr].pop()
                dfs(nxt)
            route.append(curr)
        
        dfs('JFK')
        return route[::-1]