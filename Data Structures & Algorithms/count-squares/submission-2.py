class CountSquares:

    def __init__(self):
        self.cnt = defaultdict(int)

    def add(self, point: List[int]) -> None:
        # tuple 可以直接作为字典的 key
        self.cnt[tuple(point)] += 1      

    def count(self, point: List[int]) -> int:
        x, y = point
        total = 0
        
        for (x2, y2), count in self.cnt.items():
            # 判断是否构成对角线 (水平距离 == 垂直距离)，且不是同一个点
            if abs(x - x2) == abs(y - y2) and x != x2:
                # 另外两个顶点的坐标是交错组合的
                p3_count = self.cnt.get((x, y2), 0)
                p4_count = self.cnt.get((x2, y), 0)
                
                # 三个点的数量相乘 (查询点自己算1次，不用乘)
                total += count * p3_count * p4_count
                
        return total
        
