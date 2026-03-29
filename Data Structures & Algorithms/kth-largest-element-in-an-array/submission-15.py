class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # quick select O(n)
        import random
        target = len(nums) - k

        def quickselect(l, r):
            pivot = nums[random.randint(l, r)]
            
            i, j = l, r
            
            while i <= j:
                while nums[i] < pivot:
                    i += 1
                while nums[j] > pivot:
                    j -= 1
                
                if i <= j:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                    j -= 1
            
            # 分三段：[l...j] [j+1...i-1] [i...r]
            
            if target <= j:
                return quickselect(l, j)
            elif target >= i:
                return quickselect(i, r)
            else:
                return nums[target]

        return quickselect(0, len(nums) - 1)
