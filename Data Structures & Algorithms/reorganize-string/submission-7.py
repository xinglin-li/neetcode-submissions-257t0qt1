from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        n = len(s)

        max_char = max(count, key=count.get)
        if count[max_char] > (n + 1) // 2:
            return ""

        res = [''] * n
        i = 0

        # 先放最多的
        while count[max_char] > 0:
            res[i] = max_char
            i += 2
            count[max_char] -= 1

        # 放其他
        for char in count:
            while count[char] > 0:
                if i >= n:
                    i = 1
                res[i] = char
                i += 2
                count[char] -= 1

        return "".join(res)