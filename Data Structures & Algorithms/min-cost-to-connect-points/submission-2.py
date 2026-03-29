class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        
        def manh_dist(p1, p2):
            """Calculates the Manhattan distance between two points."""
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        # Array to store the minimum cost found so far to connect each node to the MST.
        # Initialize with infinity, except for the starting node (0).
        # This replaces the need for a separate visited set and the heap/adj list.
        # min_cost_to_mst[i] = min cost to connect point[i] to the current MST.
        min_cost_to_mst = [math.inf] * N
        min_cost_to_mst[0] = 0 # Start at node 0 with 0 cost
        
        total_min_cost = 0
        nodes_in_mst = 0
        
        # While not all nodes are in the MST
        while nodes_in_mst < N:
            # 1. Find the unvisited node (u) with the smallest min_cost_to_mst
            min_edge_cost = math.inf
            u = -1 # Index of the node to add next
            
            for i in range(N):
                # We check the node only if it hasn't been added yet (min_cost_to_mst[i] != -1)
                # and its cost is less than the current best.
                if min_cost_to_mst[i] != -1 and min_cost_to_mst[i] < min_edge_cost:
                    min_edge_cost = min_cost_to_mst[i]
                    u = i
            
            # If u is -1, something is wrong, but typically this shouldn't happen 
            # until all nodes are visited (handled by the while condition).
            
            # 2. Add node u to the MST and update total cost
            total_min_cost += min_edge_cost
            nodes_in_mst += 1
            
            # Mark u as visited (using -1 to indicate it's already in the MST)
            min_cost_to_mst[u] = -1 
            
            # 3. Update the min_cost_to_mst for all unvisited neighbors (i)
            # Check every other node i against the newly added node u.
            for i in range(N):
                # If node i is unvisited (min_cost_to_mst[i] != -1)
                if min_cost_to_mst[i] != -1:
                    # Calculate the distance between the new node u and the unvisited node i
                    new_dist = manh_dist(points[u], points[i])
                    
                    # If the path through u is cheaper than the currently known cheapest path, update it
                    min_cost_to_mst[i] = min(min_cost_to_mst[i], new_dist)

        return total_min_cost

        