nums = [0,1,0,2,0,3,0,4,0,0,5,6,0,0,7,8]

n = len(nums)

temp = []

for i in range(0, n):
    if nums[i] != 0:
        temp.append(nums[i])
nt = len(temp)
for i in range(0,nt):
    nums[i] = temp[i]
for i in range(nt,n):
    nums[i] = 0

print(nums)