class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        charString = "abcdefghijklmnopqrstuvwxyz"
        beginSet = set([beginWord])
        endSet = set([endWord])
        ans = 1
        while beginSet and endSet:
            if len(beginSet) > len(endSet):
                beginSet, endSet = endSet, beginSet
            nextSet = set()
            for word in beginSet:
                for i in range(len(word)):
                    for c in charString:
                        if c == word[i]:
                            continue
                        newWord = word[:i] + c + word[i+1:]
                        if newWord in endSet:
                            return ans + 1
                        if newWord in wordSet:
                            nextSet.add(newWord)
                            wordSet.remove(newWord)
            beginSet = nextSet
            ans += 1
        return 0
                    