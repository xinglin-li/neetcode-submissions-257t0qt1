class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # 建立字符 -> 顺序 的映射
        rank = {c: i for i, c in enumerate(order)}
        
        # 比较两个单词是否按 alien 顺序排序
        def in_order(w1, w2):
            i = 0
            while i < len(w1) and i < len(w2):
                if w1[i] != w2[i]:
                    return rank[w1[i]] < rank[w2[i]]
                i += 1
            # 如果前面都相同，则短的更小
            return len(w1) <= len(w2)
        
        # 依次比较 words[i] 和 words[i+1]
        for i in range(len(words) - 1):
            if not in_order(words[i], words[i + 1]):
                return False
        
        return True

