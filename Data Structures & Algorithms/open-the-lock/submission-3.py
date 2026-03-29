class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)
        start = "0000"
        if start in dead:
            return -1
        visited = set([start])
        q = deque([(start,0)])
        while q:
            cur, depth = q.popleft()
            if cur == target:
                return depth
            for i in range(4):
                digit = int(cur[i])
                for move in (-1,1):
                    nd = str((digit+move)%10)
                    nxt = cur[:i] + nd + cur[i+1:]
                    if nxt not in dead and nxt not in visited:
                        visited.add(nxt)
                        q.append((nxt,depth+1))
        return -1