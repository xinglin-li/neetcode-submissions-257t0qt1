class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for word in strs:
            counter = [0]*26
            for ch in word:
                counter[ord(ch) - ord('a')] += 1
            print(tuple(counter))
            if tuple(counter) not in res:
                res[tuple(counter)] = [word]
            else:
                res[tuple(counter)].append(word)
        res_lst = []
        for v in res.values():
            res_lst.append(v)
        return res_lst