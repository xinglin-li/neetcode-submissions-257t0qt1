class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 核心前置优化：确保 nums1 永远是较短的那个数组
        # 理由 1：保证二分查找的时间复杂度是优异的 O(log(min(m, n)))
        # 理由 2：防止后面的 j 减出负数导致数组越界
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        
        # -------------------------------------------------------------
        # 【关键卡点 1】为什么 right = m 而不是 m - 1 ？
        # 核心本质：这里的二分查找是在找“放几个数（数量）”，而不是“索引（Index）”！
        # 长度为 m 的数组，可以往左边放 0 个、1 个...直到 m 个数。
        # 数量的选择范围是闭区间 [0, m]，总共有 m + 1 种可能，所以 right 必须初始化为 m。
        # -------------------------------------------------------------
        left, right = 0, m
        half_len = (m + n + 1) // 2  # 左半部分应该分到的总元素个数（奇数时左边多拿一个）
        
        while left <= right:
            # i 代表：当前尝试从 nums1 里面拿 i 个数放到左半边
            i = (left + right) // 2
            # j 代表：为了凑齐左半边的总数，必须从 nums2 里面拿 j 个数
            j = half_len - i
            
            # -------------------------------------------------------------
            # 【关键卡点 2】float('-inf') 和 float('inf') 的虚拟哨兵技巧
            # 既然 i 代表“个数”，那么留在左半边的最后一个数索引就是 i-1，右半边第一个数索引就是 i。
            # 如果 i == 0，说明 nums1 一个没拿，左边空了！用负无穷顶替，确保它不会大于右边的任何数。
            # 如果 i == m，说明 nums1 全拿走了，右边空了！用正无穷顶替，确保它不会小于左边的任何数。
            # -------------------------------------------------------------
            nums1_left_max = float('-inf') if i == 0 else nums1[i - 1]
            nums1_right_min = float('inf') if i == m else nums1[i]
            
            # 同理，用虚拟哨兵处理 nums2 的边界问题
            nums2_left_max = float('-inf') if j == 0 else nums2[j - 1]
            nums2_right_min = float('inf') if j == n else nums2[j]
            
            # -------------------------------------------------------------
            # 【关键卡点 3】检查是否实现了“完美对切”
            # 完美的条件是：左大组的两个最大值，都必须小于等于右大组的两个最小值
            # -------------------------------------------------------------
            if nums1_left_max <= nums2_right_min and nums2_left_max <= nums1_right_min:
                # 恭喜，切口完全正确！开始根据总长度的奇偶性计算中位数：
                
                # 情况 A：如果总元素个数是奇数，中位数就是左半边最大的那个数
                if (m + n) % 2 == 1:
                    return float(max(nums1_left_max, nums2_left_max))
                
                # 情况 B：如果总元素个数是偶数，中位数是左边最大值和右边最小值的平均数
                return (max(nums1_left_max, nums2_left_max) + min(nums1_right_min, nums2_right_min)) / 2.0
            
            elif nums1_left_max > nums2_right_min:
                # 调整切刀：nums1 拿出来的数太大了，说明切口太靠右了
                # 我们需要让 nums1 少放几个数，所以把右边界缩小
                right = i - 1
            else:
                # 调整切刀：nums2 拿出来的数太大了，说明 nums1 拿得不够多
                # 我们需要让 nums1 多放几个数，所以把左边界右移
                left = i + 1
                
        return 0.0