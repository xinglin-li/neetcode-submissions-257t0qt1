class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []

        for i in range(n):
            # Skip duplicate elements, keep only the first occurrence
            if i > 0 and nums[i] == nums[i - 1]:
                print(i)
                continue

            a = nums[i]
            l, r = i + 1, n - 1

            while l < r:
                s = a + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    ans.append([a, nums[l], nums[r]])
                    # Skip duplicates for the second and third elements
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    r -= 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

        return ans

