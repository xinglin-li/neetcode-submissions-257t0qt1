class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        # 如果目标单词根本不在字典里，直接判死刑
        if endWord not in wordSet:
            return 0
            
        # 使用集合 (Set) 存储当前层的节点，查找速度 O(1)
        beginSet = {beginWord}
        endSet = {endWord}
        length = 1
        
        while beginSet and endSet:
            # 核心优化：永远从节点较少的那个集合开始扩散
            if len(beginSet) > len(endSet):
                beginSet, endSet = endSet, beginSet
                
            nextSet = set()
            for word in beginSet:
                # 遍历当前单词的每一个字符位置
                for i in range(len(word)):
                    # 尝试将其替换为 a-z 中的任意一个字符
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        if c == word[i]:
                            continue
                            
                        # 构造出变换后的新单词
                        newWord = word[:i] + c + word[i+1:]
                        
                        # 终局判定：如果两端的水波相遇了！
                        if newWord in endSet:
                            return length + 1
                            
                        # 如果新单词在字典里，将其加入下一层的集合中
                        if newWord in wordSet:
                            nextSet.add(newWord)
                            # 从原字典中删除，相当于打上 visited 标记，防止死循环
                            wordSet.remove(newWord)
                            
            # 推进到下一层
            beginSet = nextSet
            length += 1
            
        return 0
                    