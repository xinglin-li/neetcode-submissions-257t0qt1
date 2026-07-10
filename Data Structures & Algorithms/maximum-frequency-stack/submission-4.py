class FreqStack:

    def __init__(self):
       self.freq = defaultdict(int)
       self.groups = defaultdict(list)
       self.max_freq = 0 

    def push(self, val: int) -> None:
        self.freq[val] += 1
        current_freq = self.freq[val]
        self.max_freq = max(self.max_freq, current_freq)
        self.groups[current_freq].append(val)

    def pop(self) -> int:
        val = self.groups[self.max_freq].pop()
        self.freq[val] -= 1
        if not self.groups[self.max_freq]:
            self.max_freq -= 1
        return val
        
# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()