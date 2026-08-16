class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Euler Path, 一笔画问题. Hierholzer算法. 其实就是图的后序遍历. 一笔画走到底, 然后把走过的路径压回去. 先走到底的先入队. 所以最后要reverse.
        # 1. 邻接表建图: 按字典降序排序, 后续pop()取出的即为字典序升序最小的目的地
        adj = defaultdict(list)
        for src, dst in sorted(tickets, reverse=True):
            adj[src].append(dst)
        
        route = []

        # 2. Hierholzer算法(后序DFS求解有向Euler Path)
        def dfs(curr):
            while adj[curr]:
                # 贪心取出字典序最小的目的地
                next_dst = adj[curr].pop()
                dfs(next_dst)
            # 无路可走时将节点入栈 (死胡同/终点节点最先被压入)
            route.append(curr)
        
        dfs('JFK')
        # 后续遍历结果的逆序即为答案
        return route[::-1]