def palin(s,l,r):
    if l >= r:
        return True
    if s[l] != s[r]:
        return False
    return palin(s, (l+1), (r-1))

s = 'ABCDDCBA'
n = len(s)
l = 0
r = n - 1

print(palin(s,l,r))