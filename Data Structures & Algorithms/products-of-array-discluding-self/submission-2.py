class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 每个位置的答案 = 左边所有数的乘积（prefix product）× 右边所有数的乘积（suffix product）
        n = len(nums)
        output = [1] * n

        # 1) prefix pass: output[i] = product(nums[0..i-1])
        left = 1
        for i in range(n):
            output[i] = left
            left *= nums[i]

        # 2) suffix pass: multiply by product(nums[i+1..n-1])
        right = 1
        for i in range(n - 1, -1, -1):
            output[i] *= right
            right *= nums[i]

        return output