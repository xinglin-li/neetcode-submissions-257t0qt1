class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # 1. 收集所有出现过的独立字符，初始化入度字典与邻接表
        adj = {char: set() for word in words for char in word}
        in_degree = {char: 0 for char in adj}
        
        # 2. 比较相邻单词，提取字符间的相对先后关系
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))
            
            # 特殊非法情况：前缀相同但较长的单词排在前面（如 ["abc", "ab"]）
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""
                
            for j in range(min_len):
                c1, c2 = w1[j], w2[j]
                if c1 != c2:
                    # 发现第一处不同字符，建立有向边 c1 -> c2
                    if c2 not in adj[c1]:
                        adj[c1].add(c2)
                        in_degree[c2] += 1
                    break  # 只能确定第一处不同的偏序关系，后续字符无需比较
                    
        # 3. 拓扑排序 (Kahn 算法)
        queue = deque([char for char, deg in in_degree.items() if deg == 0])
        order = []
        
        while queue:
            curr = queue.popleft()
            order.append(curr)
            
            for neighbor in adj[curr]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
                    
        # 若拓扑序列长度等于字符总数，说明无环，返回合法字母序；否则存在循环依赖
        return "".join(order) if len(order) == len(in_degree) else ""

