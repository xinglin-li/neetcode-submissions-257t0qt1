class UnionFind:

    def __init__(self, n: int):
        self.parent = list(range(n))

    def find(self, i: int) -> int:
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i: int, j: int) -> None:
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.parent[root_i] = root_j

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        uf = UnionFind(n)
        email_to_acc = {}

        for i, acc in enumerate(accounts):
            for email in acc[1:]:
                if email in email_to_acc:
                    uf.union(i, email_to_acc[email])
                else:
                    email_to_acc[email] = i
        
        leader_to_email = defaultdict(list)
        for email, acc_index in email_to_acc.items():
            root = uf.find(acc_index)
            leader_to_email[root].append(email)
        
        res = []
        for root, email in leader_to_email.items():
            name = accounts[root][0]
            res.append([name] + sorted(email))

        return res
        