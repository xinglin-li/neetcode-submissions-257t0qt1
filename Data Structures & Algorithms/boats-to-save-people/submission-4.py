class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # 核心：最重的人必须上船，能带最轻就带，不能带就自己一艘。
        people.sort()
        l, r = 0, len(people) - 1
        count = 0
        while l <= r:
            if people[l] + people[r] <= limit:
                l += 1
            r -= 1
            count += 1
        return count

