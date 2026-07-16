num = [2,3,4,5,3,4,1,3,4,2,6,7,6,2,2]

freq_dict = dict()

for i in range(0,len(num)):
    if num[i] in freq_dict: 
        freq_dict[num[i]] += 1
    else:
        freq_dict[num[i]] = 1
print(freq_dict)