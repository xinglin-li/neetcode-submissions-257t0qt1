class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # 记录 target 的三个位置是否分别被命中
        matched = [False, False, False]

        for t in triplets:
            # 剪枝：若三元组中有任何一位大于 target，使用它会导致合并结果超标
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue

            # 标记匹配到的分量
            for i in range(3):
                if t[i] == target[i]:
                    matched[i] = True

            # 提前终止
            if all(matched):
                return True

        return all(matched)
