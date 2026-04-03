class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # Topological Sort, Kahn's Algorithm.
        # 1. 提取所有出现的唯一字符，并初始化入度表
        in_degree = {c: 0 for word in words for c in word}
        adj = defaultdict(set) # 邻接表表示有向图
        
        # 2. 遍历相邻单词，构建有向图
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))
            
            # 特例拦截：如果 w1 比 w2 长，且 w2 是 w1 的前缀
            # 例如 "abcd" 排在 "abc" 前面，这是绝对不合法的字典序
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""
            
            # 寻找第一个不同的字符，建立有向边
            for j in range(min_len):
                if w1[j] != w2[j]:
                    # 如果这条边还没被添加过，才更新入度
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j])
                        in_degree[w2[j]] += 1
                    # 只有第一个不同的字符能反映顺序，后续字符无参考价值，直接 break
                    break 
        
        # 3. 拓扑排序 (BFS)
        # 将所有入度为 0 的节点（没有前置依赖的字母）加入队列
        queue = deque([c for c in in_degree if in_degree[c] == 0])
        res = []
        
        while queue:
            char = queue.popleft()
            res.append(char)
            
            # 遍历该节点指向的所有邻居
            for neighbor in adj[char]:
                in_degree[neighbor] -= 1 # 移除当前节点后，邻居的依赖减少 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor) # 邻居的依赖清空，可以入队了
        
        # 4. 检查是否有环
        # 如果结果集中的字符数量等于图中的节点总数，说明顺利排完；否则说明图中有环（存在逻辑冲突）
        if len(res) == len(in_degree):
            return "".join(res)
        else:
            return ""

