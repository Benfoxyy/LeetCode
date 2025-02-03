nums = [1,3,5,6]
target = 2

if target in nums:
    print(nums.index(target))
else:
    nums.append(target).sort()
    nums.sort()
    print(nums.index(target))