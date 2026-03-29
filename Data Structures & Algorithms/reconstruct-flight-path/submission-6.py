class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        from collections import defaultdict
        import heapq
        graph = defaultdict(list)

        # 每个 adjacency list 建成一个 min-heap
        for a, b in tickets:
            heapq.heappush(graph[a], b)

        res = []

        def dfs(cur):
            # 一直取最小目的地
            while graph[cur]:
                nxt = heapq.heappop(graph[cur])
                dfs(nxt)
            res.append(cur)

        dfs("JFK")
        return res[::-1]
        
