class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        parent = [i for i in range(n)]
        rank = [1]*n

        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        
        def union(x,y):
            px, py = find(x), find(y)
            if px == py:
                return False
            if rank[px] > rank[py]:
                parent[py] = px
            elif rank[px] < rank[py]:
                parent[px] = py
            else:
                parent[py] = px
                rank[px] += 1
            return True

        email_to_idx = {}
        for idx, account in enumerate(accounts):
            for email in account[1:]:
                if email not in email_to_idx:
                    email_to_idx[email] = idx
                else:
                    union(email_to_idx[email], idx)

        root_to_emails = defaultdict(list)
        for email, i in email_to_idx.items():
            root_to_emails[find(i)].append(email)
        
        res = []
        for i, emails in root_to_emails.items():
            user = accounts[i][0]
            emails.sort()
            res.append([user] + emails)
        
        return res



        

        

            