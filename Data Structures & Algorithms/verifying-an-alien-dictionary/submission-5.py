class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # 1. 构建字母 -> 优先级的哈希表，实现 O(1) 查询
        order_map = {char: i for i, char in enumerate(order)} 
        # 2. 依次比对相邻的两两单词
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            for j in range(len(w1)):
                # 边界情况：w1 更长且前缀与 w2 完全相同（如 "apple" 与 "app"）
                if j >= len(w2):
                    return False
                if w1[j] != w2[j]:
                    # 出现首个不匹配字符，比较字母表中的顺序
                    if order_map[w1[j]] > order_map[w2[j]]:
                        return False
                    # w1[j] < w2[j]，说明这对单词符合顺序，直接检查下一对
                    break              
        return True