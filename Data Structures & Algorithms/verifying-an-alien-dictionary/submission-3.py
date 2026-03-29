class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        rank = {c:i for i, c in enumerate(order)}
        def check_order(word1, word2):
            for i in range(min(len(word1), len(word2))):
                ch1, ch2 = word1[i], word2[i]
                if ch1 != ch2:
                    return rank[ch1] < rank[ch2]
            return len(word1) < len(word2)
        
        for i in range(len(words)-1):
            if not check_order(words[i], words[i+1]):
                return False
        return True