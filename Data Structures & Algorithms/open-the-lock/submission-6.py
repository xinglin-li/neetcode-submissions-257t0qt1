class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        from collections import deque
        deadends = set(deadends)
        if "0000" in deadends:
            return -1

        visited = set()

        def next_states(state):
            nxt_states = []
            for i in range(4):
                up = str((int(state[i]) + 1)%10)
                down = str((int(state[i]) - 1)%10)
                up_state = state[:i] + up + state[i+1:]
                down_state = state[:i] + down + state[i+1:]
                if up_state not in deadends and up_state not in visited:
                    nxt_states.append(up_state)
                if down_state not in deadends and down_state not in visited:
                    nxt_states.append(down_state)
            return nxt_states
        
        q = deque([("0000", 0)])
        visited = set(["0000"])
        while q:
            state, count = q.popleft()
            if state == target:
                return count
            for nxt_state in next_states(state):
                visited.add(nxt_state)
                q.append((nxt_state, count+1))
        return -1


        