class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # Boyer–Moore Vote Algorithm 的多候选版本
        major1 = major2 = None
        c1 = c2 = 0
        for num in nums:
            if num == major1:
                c1 += 1
            elif num == major2:
                c2 += 1
            elif c1 == 0:
                major1 = num
                c1 = 1
            elif c2 == 0:
                major2 = num
                c2 = 1
            else:
                c1 -= 1
                c2 -= 1
        c1 = c2 = 0
        res = []
        for num in nums:
            if num == major1:
                c1 += 1
            if num == major2:
                c2 += 1
        if c1 > len(nums)//3:
            res.append(major1)
        if c2 > len(nums)//3:
            res.append(major2)
        return res
