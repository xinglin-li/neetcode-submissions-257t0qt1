class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Kadane's Algorithm - Dynamic Programming Solution
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        
        Args:
            nums: list of integers
            
        Returns:
            int: maximum sum of contiguous subarray
        """
        if not nums:
            return 0
        
        max_sum = nums[0]
        current_sum = nums[0]
        
        for i in range(1, len(nums)):
            # Either extend the existing subarray or start a new one
            current_sum = max(nums[i], current_sum + nums[i])
            # Update the maximum sum seen so far
            max_sum = max(max_sum, current_sum)
        
        return max_sum

