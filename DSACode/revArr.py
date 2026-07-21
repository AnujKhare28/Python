def revArr(arr,l,r):
    if l >= r:
        return arr

    arr[l],arr[r] = arr[r],arr[l]
    return revArr(arr, (l+1), (r-1))

arr = [1,2,3,4,5,6,7,8]
l = 1
r = 6

print(revArr(arr,l,r))
