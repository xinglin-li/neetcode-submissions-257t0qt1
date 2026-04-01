class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # 将 deadends 转换为集合，实现 O(1) 的快速查找
        dead_set = set(deadends)
        
        # 边缘情况：如果初始状态 "0000" 本身就是死锁，则直接返回 -1
        if "0000" in dead_set:
            return -1
        
        # 初始化队列，存储 (当前状态, 旋转次数)
        queue = deque([("0000", 0)])
        # 记录已经访问过的状态，避免走回头路陷入死循环
        visited = set(["0000"])
        
        # 辅助函数：获取当前密码拨动一次后能产生的所有 8 个新密码
        def get_next_states(current_state):
            states = []
            for i in range(4):
                digit = int(current_state[i])
                # 向上拨动 (加 1，如果是 9 则变成 0)
                up = str((digit + 1) % 10)
                states.append(current_state[:i] + up + current_state[i+1:])
                
                # 向下拨动 (减 1，如果是 0 则变成 9)
                down = str((digit - 1) % 10)
                states.append(current_state[:i] + down + current_state[i+1:])
            return states

        # 核心 BFS 逻辑
        while queue:
            current, steps = queue.popleft()
            
            # 找到目标，返回当前步数
            if current == target:
                return steps
                
            # 遍历所有可能的下一步状态
            for next_state in get_next_states(current):
                # 如果该状态没有被访问过，且不是死锁
                if next_state not in visited and next_state not in dead_set:
                    visited.add(next_state)
                    queue.append((next_state, steps + 1))
                    
        # 如果遍历完所有可能的状态都没有找到 target，说明无法解锁
        return -1


            