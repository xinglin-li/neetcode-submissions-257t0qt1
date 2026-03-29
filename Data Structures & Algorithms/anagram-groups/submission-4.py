from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # canonical representation to constrcution hash classifier.
        groups = defaultdict(list)

        for s in strs:
            key = "".join(sorted(s))   # 核心：排序后的字符串作为hash key
            groups[key].append(s)

        return list(groups.values())