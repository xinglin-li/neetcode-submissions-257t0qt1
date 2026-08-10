class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 关键步骤 1：按区间的起点（start）升序排序
        intervals.sort(key=lambda x: x[0])
        merged = []

        for interval in intervals:
            # 如果 merged 为空，或者当前区间的起点 > 上一个已合并区间的终点
            # 说明两者完全没有重叠，直接存入 merged
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # 存在重叠：更新上一个合并区间的右端点，取两者的最大值
                merged[-1][1] = max(merged[-1][1], interval[1])
                
        return merged