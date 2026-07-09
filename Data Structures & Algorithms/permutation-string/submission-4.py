class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)

        if m > n:
            return False
        
        need = Counter(s1)
        window = defaultdict(int) 

        left = 0
        for right, ch in enumerate(s2):
            # 1. 将当前字符加入窗口
            window[ch] += 1
            
            # 2. 如果窗口大小超过了 s1 的长度，收缩左边界
            if right - left + 1 > m:
                out_ch = s2[left]  # 找到要移出的左边界字符
                window[out_ch] -= 1
                if window[out_ch] == 0:
                    del window[out_ch]  # 核心：清理计数为 0 的键，避免影响字典对比
                left += 1
            
            # 3. 检查当前窗口是否与 need 完全匹配
            if right - left + 1 == m and window == need:
                return True
        
        return False