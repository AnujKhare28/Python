num = [2,3,4,5,3,4,1,3,4,2,6,7,6,2,2]

n = len(num)

freq = dict()

for i in range(0,n):
    freq[num[i]] = freq.get(num[i],0) + 1

print(freq)