class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # quick select to select top k elements in unordered array, logn
        k = k -1
        def partition(left, right):
            pivot = nums[right]
            i = left
            for j in range(left, right):
                if nums[j] >= pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[right], nums[i] = nums[i], nums[right]
            return i
        
        def quickselect(left, right, k):
            if left >= right:
                return
            p = partition(left, right)

            if p == k:
                return 
            elif p > k:
                quickselect(left, p-1, k)
            else:
                quickselect(p+1, right, k)
        
        quickselect(0, len(nums)-1,k)
        return nums[k]


"""
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # heap. nlogk
        heap = []
        for x in nums:
            if len(heap) < k:
                heapq.heappush(heap, x)
            else:
                if x > heap[0]:
                    heapq.heapreplace(heap,x)
        return heap[0]
"""