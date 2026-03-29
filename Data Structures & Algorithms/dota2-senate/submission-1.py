class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        R = deque()
        D = deque()

        # 初始化队列
        for i, c in enumerate(senate):
            if c == 'R':
                R.append(i)
            else:
                D.append(i)

        # 模拟回合
        while R and D:
            r = R.popleft()
            d = D.popleft()

            if r < d:
                # Radiant 先出手，ban 掉这个 Dire
                R.append(r + n)
            else:
                # Dire 先出手，ban 掉这个 Radiant
                D.append(d + n)

        return "Radiant" if R else "Dire"