nums = [4,3,1,6]

class Solution:
    def isArraySpecial(self, nums: list[int]) -> bool:
        n=nums[0]%2
        for i in range(len(nums)-1):
            if n != nums[i+1]%2:
                n=nums[i+1]%2
            else:
                return False
        return True

print(Solution().isArraySpecial(nums))