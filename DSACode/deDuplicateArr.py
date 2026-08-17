nums = [1,1,1,2,3,3,4,4,4,5,6,6,7,8,8,9,10]

n = len(nums)
map = dict()

for i in range(0,n):
    map[nums[i]] = 0
j = 0
for k in map:
    nums[j] = k
    j += 1
print(j)
print(nums)