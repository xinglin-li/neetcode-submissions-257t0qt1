class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # 1) nodes: every char that appears
        adj = {c: set() for w in words for c in w}
        indeg = {c: 0 for c in adj}

        # 2) edges from first differing chars of adjacent words
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            # prefix invalid: "abc" before "ab"
            if len(w1) > len(w2) and w1.startswith(w2):
                return ""

            for a, b in zip(w1, w2):
                if a != b:
                    if b not in adj[a]:
                        adj[a].add(b)
                        indeg[b] += 1
                    break
            # if all equal up to min len, the shorter-first rule already checked above

        # 3) Kahn: queue all zero-indegree nodes
        q = deque([c for c in indeg if indeg[c] == 0])
        order = []

        while q:
            u = q.popleft()
            order.append(u)
            for v in adj[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)

        return "".join(order) if len(order) == len(indeg) else ""