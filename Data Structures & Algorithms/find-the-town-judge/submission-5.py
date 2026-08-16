class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # 统计每个节点的净得分：入度（信任他的人数）减去出度（他信任的人数）
        scores = [0] * (n + 1)

        for a, b in trust:
            scores[a] -= 1 # a 信任别人，出度 +1（得分减 1）
            scores[b] += 1 # b 被人信任，入度 +1（得分加 1）
        
        for i in range(1, n + 1):
            # 法官的特征：得分恰好为 n - 1（被所有人信任，且不信任任何人）
            if scores[i] == n - 1:
                return i
        return -1