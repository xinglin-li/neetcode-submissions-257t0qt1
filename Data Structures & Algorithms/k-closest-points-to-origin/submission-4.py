class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # heap can solve it. But there is a more efficient way of solving it.
        # quick select, which is an algorithm used to find the top k elements in an unordered array.
        # large portion of the code is identical to quick sort.

        def dist(point):
            return point[0]*point[0] + point[1]*point[1]
        
        def partition(left, right, k):
            pivot = dist(points[right])
            i = left
            for j in range(left, right):
                if dist(points[j]) <= pivot:
                    points[i], points[j] = points[j], points[i]
                    i += 1
            points[right], points[i] = points[i], points[right]
            return i
        
        def quick_select(left, right, k):
            if left >= right:
                return
            p = partition(left, right, k)
            if p >= k:
                return
            else:
                quick_select(p+1, right, k)
        
        quick_select(0, len(points)-1, k)
        return points[:k]