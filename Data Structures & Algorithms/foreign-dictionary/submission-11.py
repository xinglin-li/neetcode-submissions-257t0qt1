class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = defaultdict(set)
        indegree = {char: 0 for word in words for char in word}
        # construct graph
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i+1]
            if len(word1) > len(word2) and word1.startswith(word2):
                return ""
            
            for char1, char2 in zip(word1, word2):
                # the loop is break onece we find the first char1 != char2
                if char1 != char2:
                    if char2 not in graph[char1]:
                        graph[char1].add(char2)
                        indegree[char2] += 1
                    break

        # topological sort
        queue = deque(char for char in indegree if indegree[char] == 0)
        order = []
        while queue:
            char = queue.popleft()
            order.append(char)
            for nei in graph[char]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        
        if len(order) != len(graph):
            return ""
        
        return "".join(order)

