class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {}      # email -> parent email
        owner = {}       # email -> user name

        # 1️⃣ 初始化：为每个 email 建立 parent 并记录所属用户
        for acc in accounts:
            name = acc[0]
            for email in acc[1:]:
                parent.setdefault(email, email)
                owner[email] = name

        # 2️⃣ Union-Find 基础函数
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])   # 路径压缩
            return parent[x]

        def union(a, b):
            parent[find(a)] = find(b)

        # 3️⃣ 把同一个账号里出现的 email 合并
        for acc in accounts:
            first = acc[1]
            for email in acc[2:]:
                union(first, email)

        # 4️⃣ 收集每个 root 下的 email 组
        groups = collections.defaultdict(list)
        for email in parent:
            root = find(email)
            groups[root].append(email)

        # 5️⃣ 输出格式：名字 + 排序过的 email
        res = []
        for root, emails in groups.items():
            res.append([owner[root]] + sorted(emails))
        return res