class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()

        left, right = 0, n - 1
        while left < right:
            mid = (left + right)//2
            # dy/dx > 0
            if mountainArr.get(mid) < mountainArr.get(mid+1):
                left = mid + 1
            # dy/dx <= 0
            else:
                right = mid
        peak = left

        def binary_search_left(l, r):
            while l <= r:
                mid = (l+r)//2
                num = mountainArr.get(mid)
                if num == target:
                    return mid
                if num < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return -1
        
        index = binary_search_left(0, peak)
        if index != -1:
            return index
        
        def binary_search_right(l,r):
            while l <= r:
                mid = (l+r)//2
                num = mountainArr.get(mid)
                if num == target:
                    return mid
                if num < target:
                    r = mid - 1
                else:
                    l = mid + 1
            return -1
        return binary_search_right(peak,n-1)