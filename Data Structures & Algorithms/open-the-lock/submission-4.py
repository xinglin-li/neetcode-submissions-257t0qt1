class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)
        start = "0000"
        
        # 起点就是死锁，直接失败
        if start in dead:
            return -1
        # 已经是目标
        if start == target:
            return 0
        
        # 生成某个状态的所有邻居（一次拨动）
        def neighbors(state: str) -> List[str]:
            res = []
            s = list(state)
            for i in range(4):
                digit = int(s[i])
                # 往上拨一格
                up = (digit + 1) % 10
                s[i] = str(up)
                res.append("".join(s))
                # 往下拨一格
                down = (digit - 1) % 10
                s[i] = str(down)
                res.append("".join(s))
                # 复原这一位，继续处理下一位
                s[i] = str(digit)
            return res
        
        q = deque()
        q.append(start)
        visited = set([start])
        steps = 0
        
        while q:
            # 当前层的所有节点
            for _ in range(len(q)):
                cur = q.popleft()
                if cur == target:
                    return steps
                if cur in dead:
                    continue
                for nxt in neighbors(cur):
                    if nxt not in visited and nxt not in dead:
                        visited.add(nxt)
                        q.append(nxt)
            steps += 1
        
        return -1