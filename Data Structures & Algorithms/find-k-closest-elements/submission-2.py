class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # 二分法找区间起点
        left, right = 0, len(arr) - k
        
        while left < right:
            mid = (left + right)//2
            # mid is left point, then arr[mid], arr[mid+1] ..., arr[mid+k-1] are in the range
            # comparing arr[mid: mid+k] and arr[mid+1:mid+k+1]
            # 其他元素都是公共的, 只有 arr[mid] and arr[mid+k+1] 不是公共的
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid
        
        return arr[left: left + k]