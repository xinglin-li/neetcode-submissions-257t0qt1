class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # 到达第 i 阶的最小花费取决于从 i-1 或 i-2 踏上来的花费
        # 初始站在第 0 阶和第 1 阶不需要额外花费
        prev2, prev1 = 0, 0
        
        for c in cost:
            # 踩上当前台阶并准备向后的总花费
            curr = c + min(prev1, prev2)
            prev2, prev1 = prev1, curr
            
        # 最终可以从倒数第一阶或倒数第二阶直接迈出楼顶
        return min(prev1, prev2)