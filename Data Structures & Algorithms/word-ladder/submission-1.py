from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # 1. endWord 不在字典里，直接无解
        if endWord not in wordList:
            return 0
        
        L = len(beginWord)
        
        # 2. 建“通配符模式” -> 单词列表 的映射
        #   比如 hot -> *ot, h*t, ho*
        pattern_dict = defaultdict(list)
        for word in wordList:
            for i in range(L):
                pattern = word[:i] + "*" + word[i+1:]
                pattern_dict[pattern].append(word)
        
        # 3. BFS
        queue = deque([(beginWord, 1)])  # (当前单词, 当前层数/长度)
        visited = set([beginWord])
        
        while queue:
            word, level = queue.popleft()
            
            # 对当前 word 的每一个通配符模式，找“邻居单词”
            for i in range(L):
                pattern = word[:i] + "*" + word[i+1:]
                
                for nei in pattern_dict[pattern]:
                    if nei == endWord:
                        return level + 1      # 下一步就到终点
                    if nei not in visited:
                        visited.add(nei)
                        queue.append((nei, level + 1))
                
                # 这一行很重要：该 pattern 用完就清空，避免重复遍历
                pattern_dict[pattern] = []
        
        return 0

