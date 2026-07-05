class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # Boyer–Moore Vote Algorithm 的多候选版本
        # 1st pass: 找两个候选人
        cand1 = None
        cand2 = None
        count1 = 0
        count2 = 0

        for x in nums:
            if x == cand1:
                count1 += 1
            elif x == cand2:
                count2 += 1
            elif count1 == 0:
                cand1 = x
                count1 = 1
            elif count2 == 0:
                cand2 = x
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
        # 2nd pass: 重新计数（只看这两个候选）
        ans = []
        for cand in (cand1, cand2):
            if cand is not None and nums.count(cand) > len(nums)//3:
                ans.append(cand)
        return ans