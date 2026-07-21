def facto(num):
    if num == 0 or num == 1:
        return 1
    return num * facto(num -1)

print(facto(3)) 

print(facto(7)) 
