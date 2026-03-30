class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return -1

        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh_count = 0

        # 1. 扫描网格，将所有腐烂的水果加入队列，并统计新鲜水果数量
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_count += 1

        # 如果一开始就没有新鲜水果，直接返回 0 分钟
        if fresh_count == 0:
            return 0

        minutes = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # 2. 开始多源广度优先搜索
        while queue:
            # rotten_this_minute 标记这一分钟内是否有新的水果被传染腐烂
            rotten_this_minute = False
            
            # 按层遍历：只处理当前队列中已有的元素（即同一分钟内腐烂的水果）
            for _ in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    
                    # 如果相邻位置在边界内，且是新鲜水果
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2       # 将其标记为腐烂
                        fresh_count -= 1       # 新鲜水果数量减一
                        queue.append((nr, nc)) # 加入队列，下一分钟它将成为传染源
                        rotten_this_minute = True
            
            # 如果这一分钟内发生了传染，时间增加 1 分钟
            if rotten_this_minute:
                minutes += 1

        # 3. 搜索结束后，如果还有新鲜水果没被感染，返回 -1；否则返回经过的时间
        return minutes if fresh_count == 0 else -1