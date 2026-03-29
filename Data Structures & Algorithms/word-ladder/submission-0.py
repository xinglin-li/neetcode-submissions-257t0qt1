class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        L = len(beginWord)

        pattern_dict = defaultdict(list)
        for word in wordList:
            for i in range(L):
                pattern = word[:i] + '*' + word[i+1:]
                pattern_dict[pattern].append(word)
        
        q = deque([(beginWord,1)])
        visited = set([beginWord])

        while q:
            word, level = q.popleft()
            for i in range(L):
                pattern = word[:i] + "*" + word[i+1:]
                for nei in pattern_dict[pattern]:
                    if nei == endWord:
                        return level + 1
                    if nei not in visited:
                        visited.add(nei)
                        q.append((nei, level + 1))
                pattern_dict[pattern] = []
        return 0
