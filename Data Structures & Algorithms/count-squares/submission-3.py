class CountSquares:

    def __init__(self):
        # 记录每个坐标点出现的频次, (x, y) -> count
        self.point_counts = defaultdict(int)
        # 记录 x 坐标下对应的所有 y 坐标集合, 用于加速对同列点的查找
        self.x_to_ys = defaultdict(set)

    def add(self, point: List[int]) -> None:
        x, y = point
        self.point_counts[(x, y)] += 1
        self.x_to_ys[x].add(y)

    def count(self, point: List[int]) -> int:
        px, py = point
        total_squares = 0
        if px not in self.x_to_ys:
            return 0
        # 遍历查询处于同一条垂线上的所有点, x = px -> (px, y)
        for y in self.x_to_ys[px]:
            if y == py:
                continue # 边长必须 > 0
            side = abs(y - py)
            for nx in (px + side, px - side):
                # 统计构成正方形的另外三个点的出现频次并取乘积
                # 三个顶点坐标分别为：(px, y), (nx, py), (nx, y)
                c1 = self.point_counts[(px, y)]
                c2 = self.point_counts[(nx, py)]
                c3 = self.point_counts[(nx, y)]

                total_squares += c1 * c2 * c3

        return total_squares
