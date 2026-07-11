class TimeMap:

    def __init__(self):
        self.arr = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.arr[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        target_arr = self.arr[key]
        l, r = 0, len(target_arr) - 1

        while l <= r:
            mid = l + (r - l) // 2
            ts = target_arr[mid][0]
            if ts <= timestamp:
                l = mid + 1
            else:
                r = mid - 1
        
        return target_arr[r][1] if r >= 0 else ""
