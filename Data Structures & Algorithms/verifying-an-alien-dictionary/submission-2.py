class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # 1. 记录每个外星字母的顺序权重
        order_map = {char: index for index, char in enumerate(order)}
        
        # 2. 遍历并比较相邻的单词对
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            
            # 3. 逐字符进行比较
            for j in range(min(len(word1), len(word2))):
                if word1[j] != word2[j]:
                    # 发现不同字符，比较其在外星字典中的大小
                    if order_map[word1[j]] > order_map[word2[j]]:
                        return False
                    # 顺序正确，不需要再比较这两个单词的后续字符
                    break
            else:
                # 如果循环正常结束（即没有遇到 break，说明前面字符都一样）
                # 检查是否出现了类似 "apple" 在 "app" 前面的情况
                if len(word1) > len(word2):
                    return False
                    
        return True