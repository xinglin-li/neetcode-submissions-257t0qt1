from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.dictionary = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dictionary[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dictionary.keys():
            return ""
        l,r = 0, len(self.dictionary[key]) - 1
        res = ""
        while l <= r:
            mid = (l+r)//2
            if self.dictionary[key][mid][0] <= timestamp:
                res = self.dictionary[key][mid][1]
                l = mid + 1
            elif self.dictionary[key][mid][0] > timestamp:
                r = mid - 1
        return res
