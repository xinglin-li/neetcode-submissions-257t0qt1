class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        # 初始化并查集：节点为账户的索引 0 到 n-1
        parent = list(range(n))
        rank = [1] * n
        
        # 你的教科书级 find：迭代 + 隔代压缩 (Path Halving)
        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
            
        # 你的教科书级 union：按秩合并 (Union by Rank)
        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return False
            
            if rank[px] > rank[py]:
                parent[py] = px
            else:
                parent[px] = py
                if rank[px] == rank[py]:
                    rank[py] += 1
            return True

        # 1. 遍历邮箱，进行合并
        # email_to_account_idx 记录每个 email 对应的账户索引
        email_to_account_idx = {}
        for i, account in enumerate(accounts):
            # account[0] 是名字，account[1:] 是邮箱
            for email in account[1:]:
                if email in email_to_account_idx:
                    # 如果邮箱之前出现过，将当前账户与之前的账户合并
                    union(i, email_to_account_idx[email])
                else:
                    # 如果没出现过，记录这个邮箱属于账户 i
                    email_to_account_idx[email] = i
                    
        # 2. 将所有邮箱归类到它们的“根账户”下
        root_to_emails = collections.defaultdict(list)
        for email, account_idx in email_to_account_idx.items():
            # 找到该账户对应的根节点
            root = find(account_idx)
            root_to_emails[root].append(email)
            
        # 3. 格式化输出：排序邮箱，并加上名字
        res = []
        for root, emails in root_to_emails.items():
            # 题目要求邮箱内部按字母顺序排序
            sorted_emails = sorted(emails)
            name = accounts[root][0]
            res.append([name] + sorted_emails)
            
        return res



        

        

            