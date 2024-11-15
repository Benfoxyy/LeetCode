nums = [-1,0,0,0,0,3,3]
nums.clear()
nums.extend(list(set(nums)))
nums.sort()
print(nums)