class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # 1. Manhatten Distance function
        def manh_dist(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        N = len(points)
        
        # 2. Build the Adjacency List (Graph)
        # graph[i] = list of (cost, neighbor_index)
        # We don't need heaps here, just a simple list is fine.
        adj = defaultdict(list)
        for i in range(N):
            for j in range(i + 1, N):
                d = manh_dist(points[i], points[j])
                adj[i].append((d, j))
                adj[j].append((d, i))
        
        # 3. Prim's Algorithm Setup
        # Min-Heap (Priority Queue) stores (cost, node_index)
        # Start at point 0. Initial cost to reach it is 0.
        min_heap = [(0, 0)]
        
        visited = set()
        min_cost = 0
        
        # 4. Main Loop
        # The loop runs until we've visited all N nodes.
        while len(visited) < N:
            # Pop the edge with the minimum cost from the heap
            cost, u = heapq.heappop(min_heap)
            
            # If the node is already in the MST (visited), skip it.
            if u in visited:
                continue
            
            # Add the node to the MST
            visited.add(u)
            min_cost += cost
            
            # Explore neighbors of the newly added node u
            for edge_cost, v in adj[u]:
                # If neighbor v is not yet in the MST, push its edge onto the heap
                if v not in visited:
                    heapq.heappush(min_heap, (edge_cost, v))
                    
        return min_cost


        