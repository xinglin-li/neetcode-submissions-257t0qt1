class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # Boyer–Moore Vote Algorithm 的多候选版本
        # 1st pass: 找两个候选人
        cand1 = cand2 = None
        c1 = c2 = 0
        for x in nums:
            if x == cand1:
                c1 += 1
            elif x == cand2:
                c2 += 1
            elif c1 == 0:
                cand1, c1 = x, 1
            elif c2 == 0:
                cand2, c2 = x, 1
            else:
                c1 -= 1
                c2 -= 1

        # 2nd pass: 重新计数（只看这两个候选）
        c1 = c2 = 0
        for x in nums:
            if x == cand1:
                c1 += 1
            elif x == cand2:
                c2 += 1

        res = []
        n = len(nums)
        if c1 > n // 3:
            res.append(cand1)
        if c2 > n // 3:
            res.append(cand2)
        return res
