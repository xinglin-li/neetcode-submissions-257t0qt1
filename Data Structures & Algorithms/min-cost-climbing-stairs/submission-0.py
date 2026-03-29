class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # min[i] = min(min[i-1], min[i-2]) + cost[i]
        n = len(cost)
        cum_min_cost = [float('inf')]*n
        for i in range(n):
            if i == 0 or i == 1:
                cum_min_cost[i] = cost[i]
            else:
                cum_min_cost[i] =  min(cum_min_cost[i-1], cum_min_cost[i-2]) + cost[i]
        return min(cum_min_cost[n-1], cum_min_cost[n-2])