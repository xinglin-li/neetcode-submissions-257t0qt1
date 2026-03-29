class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        from collections import defaultdict
        graph = defaultdict(list)

        for from_i, to_i in tickets:
            graph[from_i].append(to_i)
        for node in graph:
            graph[node].sort(reverse=True)

        res = []

        def dfs(cur):
            while graph[cur]:
                nxt = graph[cur].pop()
                dfs(nxt)
            res.append(cur)
        
        dfs("JFK")
        return res[::-1]
        
