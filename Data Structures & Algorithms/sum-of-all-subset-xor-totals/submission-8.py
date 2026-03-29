class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        #如果用这个方法解释，就不是一个简单题
        #只要一个bit位出现过一次1，那么所有组合里，必定有2^(n-1)次出现过奇数次1
        #XOR=1，如果出现奇数次1. Otherwise, 0
        #Summation, is a count of how many 1's in a bit. So you can multiply by 2^(n-1)
        total_xor = 0
        for num in nums:
            total_xor |= num
        return total_xor*(1 << (len(nums)-1))