class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        from collections import defaultdict
        graph = defaultdict(list)

        # 1. 将每个 from -> to 存入 graph，并按字典序排序
        for a, b in tickets:
            graph[a].append(b)
        for k in graph:
            graph[k].sort()  # 保证每次取最小的目的地

        res = []

        # 2. DFS(Hierholzer) 找欧拉路径
        def dfs(cur):
            # 依次用完所有出边
            while graph[cur]:
                nxt = graph[cur].pop(0)   # 总是取字典序最小的
                dfs(nxt)
            # 当前节点加入结果（倒序）
            res.append(cur)

        dfs("JFK")
        return res[::-1]
