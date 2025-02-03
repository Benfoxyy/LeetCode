nums = [4,2,4,0,0,3,0,5,1,0]

for i in range(nums.count(0)):
    nums.remove(0)
    nums.append(0)
    
print(nums)