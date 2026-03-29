class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # heap can solve it. But there is a more efficient way of solving it.
        # quick select, which is an algorithm used to find the top k elements in an unordered array.
        # large portion of the code is identical to quick sort.
        def dist(p):
            return p[0]*p[0] + p[1]*p[1]

        # Lomuto partition
        def partition(left, right):
            pivot = dist(points[right])
            i = left
            for j in range(left, right):
                if dist(points[j]) <= pivot:
                    points[i], points[j] = points[j], points[i]
                    i += 1
            points[i], points[right] = points[right], points[i]
            return i

        def quickselect(left, right, k):
            if left >= right:
                return

            p = partition(left, right)

            if p == k: 
                return
            elif p < k:
                quickselect(p + 1, right, k)
            else:
                quickselect(left, p - 1, k)

        quickselect(0, len(points)-1, k)
        return points[:k]