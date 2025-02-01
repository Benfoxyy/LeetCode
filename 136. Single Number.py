nums = [1,0,1]

for i in set(nums):
    nums.remove(i)
    if i not in nums:
        print(i)