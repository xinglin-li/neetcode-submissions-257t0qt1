class CountSquares:

    def __init__(self):
        self.cnt = defaultdict(int)

    def add(self, point: List[int]) -> None:
        x, y = point
        self.cnt[(x, y)] += 1       

    def count(self, point: List[int]) -> int:
        x, y = point
        res = 0

        for (x2, y2), c in self.cnt.items():
            # 必须是同一列 + 不能是同一个点
            if x2 == x and y2 != y:
                d = y2 - y

                # 右边
                res += c * self.cnt.get((x+d,y),0) * self.cnt.get((x+d,y2),0) 

                # 左边
                res += c * self.cnt.get((x-d,y),0) * self.cnt.get((x-d,y2),0) 
        return res