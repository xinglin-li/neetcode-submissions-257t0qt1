class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = tank = start = 0
        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            tank += diff
            total += diff
            if tank < 0:
                # for index between s and i
                # suppose diff[s] - cost[s] > 0, then you should not drop it.
                # suppose diff[s] - cost[s] < 0, then you cannot start from it.
                start = i + 1
                tank = 0
        return start if total >= 0 else -1