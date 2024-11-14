nums = [6,6,6,7,7]
m = {}
c = round(len(nums)/2)
for i in set(nums):
    count = nums.count(i)
    if count >= c:
        m[i] = count
    
print(max(m, key=m.get))