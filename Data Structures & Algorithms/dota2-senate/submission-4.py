class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        radient = deque()
        dire = deque()

        for i, s in enumerate(senate):
            if s == "R":
                radient.append(i)
            else:
                dire.append(i)
        
        while radient and dire:
            r = radient.popleft()
            d = dire.popleft()

            if r < d:
                radient.append(r + n)
            else:
                dire.append(d + n)
        
        return "Radiant" if radient else "Dire"