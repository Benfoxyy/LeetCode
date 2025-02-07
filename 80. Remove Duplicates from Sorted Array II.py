nums = [1,1,1,2,2,3]

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        for i in set(nums):
            if nums.count(i) > 2:
                for _ in range(nums.count(i)-2):
                    nums.remove(i)
        k = len(nums)
        return k
        
print(Solution().removeDuplicates(nums))