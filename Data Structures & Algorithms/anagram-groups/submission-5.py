from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # canonical representation to constrcution hash classifier.
        # 不用排序，直接用 26字母计数向量作为 key
        groups = defaultdict(list)

        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c)-ord('a')] += 1
            key = tuple(count)
            groups[key].append(s)

        return list(groups.values())