class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends_set = set(deadends)
        if "0000" in deadends_set:
            return -1
        q = deque([(["0","0","0","0"],0)])
        visited = set()
        while q:
            lock_nums, res = q.popleft()
            for i in [1,-1]:
                for j in range(4):
                    lock_nums_temp = lock_nums.copy()
                    lock_nums_temp[j] = str((int(lock_nums[j]) + i) % 10)
                    lock_num = "".join(lock_nums_temp)
                    if lock_num in visited:
                        continue 
                    if lock_num == target:
                        return res + 1
                    if lock_num not in deadends_set:
                        visited.add(lock_num)
                        q.append((list(lock_num),res + 1))
        return -1