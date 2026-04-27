class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r = deque()
        d = deque()
        for i, c in enumerate(senate):
            if c == "R":
                r.append(i)
            else:
                d.append(i)
        n = len(senate)
        while r and d:
            r_idx = r.popleft()
            d_idx = d.popleft()
            if r_idx < d_idx:
                r.append(r_idx + n)
            else:
                d.append(d_idx + n)

        return "Radiant" if r else "Dire"

