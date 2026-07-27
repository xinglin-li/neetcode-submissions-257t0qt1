class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # 将 deadends 转换为集合，实现 O(1) 的快速查找
        deadends = set(deadends)
        # 边缘情况：如果初始状态 "0000" 本身就是死锁，则直接返回 -1
        if "0000" in deadends:
            return -1
        # 初始化队列，存储 (当前状态, 旋转次数)
        q = deque([("0000", 0)])
        # 记录已经访问过的状态，避免走回头路陷入死循环
        visited = set(["0000"])
        
        # 辅助函数：获取当前密码拨动一次后能产生的所有 8 个新密码
        def next_states(curr_state):
            states = []
            for i in range(4):
                # 向上拨动 (加 1，如果是 9 则变成 0)
                nxt_num = (int(curr_state[i]) + 1) % 10
                state = curr_state[:i] + str(nxt_num) + curr_state[i+1:]
                states.append(state)
            for i in range(4):
                # 向下拨动 (减 1，如果是 0 则变成 9)
                nxt_num = (int(curr_state[i]) - 1) % 10
                state = curr_state[:i] + str(nxt_num) + curr_state[i+1:]
                states.append(state)
            return states

        # 核心 BFS 逻辑
        while q:
            # 找到目标，返回当前步数
            curr_state, step = q.popleft()
            if curr_state == target:
                return step    
            # 遍历所有可能的下一步状态
            for state in next_states(curr_state):
                # 如果该状态没有被访问过，且不是死锁
                if state not in visited and state not in deadends:
                    visited.add(state)
                    q.append((state, step + 1))
                    
        # 如果遍历完所有可能的状态都没有找到 target，说明无法解锁
        return -1


            