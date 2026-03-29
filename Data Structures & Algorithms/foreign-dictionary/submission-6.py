class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c:set() for w in words for c in w}
        indeg = {c:0 for c in adj}

        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            if len(w1) > len(w2) and w1.startswith(w2):
                return ""
            for a,b in zip(w1,w2):
                if a != b:
                    if b not in adj[a]:
                        adj[a].add(b)
                        indeg[b] += 1
                    break
            
        q = deque([c for c in indeg if indeg[c] == 0])
        order = []
        # suppose c's indeg == 0, it will not be visited again
        while q:
            c = q.popleft()
            order.append(c)
            for v in adj[c]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)
        return "".join(order) if len(order) == len(indeg) else ""
            