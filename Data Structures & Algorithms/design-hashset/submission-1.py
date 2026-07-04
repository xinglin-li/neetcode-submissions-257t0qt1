class MyHashSet:

    def __init__(self):
        self.size = 1009
        self.buckets = [[] for _ in range(self.size)]
    
    def _hash(self, key: int) -> int:
        return key % self.size

    def add(self, key: int) -> None:
        h = self._hash(key)
        if key not in self.buckets[h]:
            self.buckets[h].append(key)

    def remove(self, key: int) -> None:
        h = self._hash(key)
        if key in self.buckets[h]:
            self.buckets[h].remove(key)

    def contains(self, key: int) -> bool:
        return key in self.buckets[self._hash(key)]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)