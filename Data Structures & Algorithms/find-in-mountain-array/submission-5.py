class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()
        
        # -------------------------------------------------------------
        # 【第一步】二分查找：寻找山顶（Peak）的索引
        # 这里的二分依据是：看当前位置是处于“上坡”还是“下坡”
        # -------------------------------------------------------------
        left, right = 0, n - 1
        peak = 0
        while left <= right:
            mid = (left + right) // 2
            # 为了判断趋势，我们拿 mid 和它右边邻居 mid + 1 比大小
            # 注意：由于 mid 永远小于 right，且山顶不在两端，这里 mid+1 不会越界
            if mountainArr.get(mid) < mountainArr.get(mid + 1):
                # 说明还在“上坡”，山顶一定在 mid 右边（不包含 mid）
                left = mid + 1
            else:
                # 说明已经在“下坡”或者是山顶，山顶在 mid 左边（包含 mid）
                peak = mid
                right = mid - 1
                
        # -------------------------------------------------------------
        # 【第二步】二分查找：在左侧“递增区间” [0, peak] 寻找 target
        # 这是最普通的二分查找，因为题目要最小索引，所以先找左边
        # -------------------------------------------------------------
        left, right = 0, peak
        while left <= right:
            mid = (left + right) // 2
            val = mountainArr.get(mid)
            if val == target:
                return mid  # 找到了直接返回
            elif val < target:
                left = mid + 1
            else:
                right = mid - 1
                
        # -------------------------------------------------------------
        # 【第三步】二分查找：在右侧“递减区间” [peak + 1, n - 1] 寻找 target
        # 【关键卡点】：这里的区间是“单调递减”的！
        # 意味着：如果 val < target，说明我们走得太远、数字太小了，切刀应该往左移（right = mid - 1）
        # -------------------------------------------------------------
        left, right = peak + 1, n - 1
        while left <= right:
            mid = (left + right) // 2
            val = mountainArr.get(mid)
            if val == target:
                return mid
            elif val < target:
                # 递减区间特性：数字小了，反而要往左边找更大的数
                right = mid - 1
            else:
                # 数字大了，往右边找更小的数
                left = mid + 1
                
        return -1