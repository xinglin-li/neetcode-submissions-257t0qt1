class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_map = {ch: idx for idx, ch in enumerate(order)}

        def in_order(w1, w2):
            i = 0
            while i < len(w1) and i < len(w2):
                c1, c2 = w1[i], w2[i]
                if c1 != c2:
                    return order_map[c1] < order_map[c2]
                i += 1
            return len(w1) <= len(w2)
        
        for i in range(len(words)-1):
            if not in_order(words[i], words[i+1]):
                return False
        return True

