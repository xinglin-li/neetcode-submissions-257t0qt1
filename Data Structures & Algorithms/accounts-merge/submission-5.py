class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {}
        owner = {}
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                owner[email] = name
                parent.setdefault(email,email)
        
        def find(email):
            if email != parent[email]:
                parent[email] = find(parent[email])
            return parent[email]
        
        def union(a, b):
            parent[find(a)] = find(b)
        
        for account in accounts:
            first = account[1]
            for email in account[2:]:
                union(first, email)

        groups = defaultdict(list)
        for email in parent:
            root = find(email)
            groups[root].append(email)

        res = []
        for root, emails in groups.items():
            name = owner[root]
            res.append([name] + sorted(emails))
        return res     