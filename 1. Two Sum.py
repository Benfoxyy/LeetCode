nums = [3,2,3]
target = 6

for idx,i in enumerate(nums):
    num = target - i
    nums[idx] = None
    if num in nums:
        print(idx,nums.index(num))