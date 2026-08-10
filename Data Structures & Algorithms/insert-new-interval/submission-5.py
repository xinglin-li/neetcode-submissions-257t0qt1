class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for interval in intervals:
            # 情况 1：当前区间的终点 < 新区间的起点
            # 说明当前区间完全在新区间的左边，不可能重叠，直接放入结果
            if interval[1] < newInterval[0]:
                res.append(interval)
            
            # 情况 2：当前区间的起点 > 新区间的终点
            # 说明当前区间完全在新区间的右边，此时 newInterval 已经合并完毕，可以存入 res
            # 然后把当前区间变成“新的待插入区间”，继续往后处理
            elif interval[0] > newInterval[1]:
                res.append(newInterval)
                newInterval = interval # 更新待插入区间为当前的 interval
            
            # 情况 3：有重叠（既不在左也不在右）
            # 不断扩充 newInterval 的边界，取两者的最小起点和最大终点
            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])
        # 循环结束后，把最后一个还没放进去的 newInterval 追加到末尾
        res.append(newInterval)
        return res
            
