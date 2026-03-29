class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends_set = set(deadends)
        start = ["0","0","0","0"]
        
        # 先判断起点是否在 deadends
        if "".join(start) in deadends_set:
            return -1
        
        visited = set(["0000"])
        q = deque([(start, 0)])
        
        while q:
            lock_nums, res = q.popleft()
            
            for i in [1, -1]:
                for j in range(4):
                    lock_nums_temp = lock_nums.copy()
                    lock_nums_temp[j] = str((int(lock_nums[j]) + i) % 10)
                    lock_num = "".join(lock_nums_temp)
                    
                    if lock_num == target:
                        return res + 1
                    
                    if lock_num not in deadends_set and lock_num not in visited:
                        visited.add(lock_num)
                        q.append((list(lock_num), res + 1))
        
        return -1