class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        timestamp = [0] * 1001
        for num, start, end in trips:
            timestamp[start] += num
            timestamp[end] -= num
        
        curr_passenger = 0
        for num in timestamp:
            curr_passenger += num
            if curr_passenger > capacity:
                return False
        
        return True