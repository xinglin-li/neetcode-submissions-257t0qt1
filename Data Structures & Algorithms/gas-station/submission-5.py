class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # 如果总油量小于总消耗，一定无解。
        # 如果从 start 出发，到 i 时油量变成负数，那么 start...i 中的任何位置都不可能作为起点。
        total = 0
        tank = 0
        start = 0

        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            total += diff
            tank += diff

            if tank < 0:
                start = i + 1
                tank = 0
        
        return start if total >= 0 else -1