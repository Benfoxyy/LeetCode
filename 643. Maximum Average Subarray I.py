nums = [7,4,5,8,8,3,9,8,7,6]
k = 7

class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        # Compute initial sum of the first k elements
        subscriptable = sum(nums[:k])
        max_sum = subscriptable  # Track the max sum found

        # Slide the window across the array
        for i in range(k, len(nums)):
            subscriptable += nums[i] - nums[i - k]  # Update sum in O(1)
            max_sum = max(max_sum, subscriptable)  # Keep track of max sum

        return max_sum / k  # Compute and return max average

        
print(Solution().findMaxAverage(nums, k))