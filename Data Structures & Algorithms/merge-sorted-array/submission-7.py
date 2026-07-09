class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 倒序双指针
        # Similar to the merge function of merge sort algorithm, but remember to start merge from right
        # 这个题恶心的点是题目很长, 最后才说明必须是把 nums2 merge into nums1 in-place. 所以必须倒序.
        i = m - 1
        j = n - 1
        k = m + n - 1
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        

        
