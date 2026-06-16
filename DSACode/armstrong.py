n = 1535
num = n
result  = 0
nod = len(str(n))
while num > 0:
    ld = num % 10
    result = result +ld ** nod
    num = num // 10
print(n == result)