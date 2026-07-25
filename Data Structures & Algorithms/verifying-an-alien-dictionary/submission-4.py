class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_map = {ch : i for i, ch in enumerate(order)}

        for i in range(len(words)-1):
            word1, word2 = words[i], words[i+1]
            for j in range(len(word1)):
                if j >= len(word2):
                    return False
                if order_map[word1[j]] >  order_map[word2[j]]:
                    return False
                if order_map[word1[j]] <  order_map[word2[j]]:
                    break
        return True