class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # 1. 统计每个任务出现的频次
        task_counts = Counter(tasks)
        
        # 2. 找出最高频次 max_freq
        max_freq = max(task_counts.values())
        
        # 3. 统计有多少个任务达到了最高频次 max_freq
        max_freq_count = sum(1 for count in task_counts.values() if count == max_freq)
        
        # 4. 根据数学桶公式计算最小周期数
        part_time = (max_freq - 1) * (n + 1) + max_freq_count
        
        # 5. 取计算值与任务总长度的最大值
        return max(len(tasks), part_time)
