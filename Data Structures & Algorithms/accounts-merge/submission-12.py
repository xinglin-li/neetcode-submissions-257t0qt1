class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {}
        email_to_name = {}

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        # 1. 构建邮箱并查集, 以及邮箱到名字的映射
        for account in accounts:
            name = account[0]
            first_email = account[1]
            for email in account[1:]:
                if email not in parent:
                    parent[email] = email
                email_to_name[email] = name
                # 将同一账户下的所有邮箱与第一个邮箱合并
                root_first, root_curr = find(first_email), find(email)
                if root_first != root_curr:
                    parent[root_curr] = root_first
        # 2. 将属于同一集合根节点的邮箱聚合
        groups = defaultdict(list)
        for email in parent:
            root = find(email)
            groups[root].append(email)
        
        # 3. 排序邮箱并组装最终结果
        return [[email_to_name[root]] + sorted(emails) for root, emails in groups.items()]