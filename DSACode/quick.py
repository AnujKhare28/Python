def partition(nums, l, h):
    pivot = nums[l]
    i = l
    j = h

    while i < j:

        while nums[i] <= pivot and i <= h - 1:
            i += 1
        while nums[j] > pivot and j >= l + 1:
            j -= 1
        if i < j:
             nums[i], nums[j] = nums[j], nums[i]
        
        nums[l], nums[j] = nums[j], nums[l]
        return j
        
def quick(nums, l, h):
    if l < h:
        idx = partition(nums, l, h)
        quick(nums, l, idx-1)
        quick(nums, idx+1, h)

arr = [5,7,8,4,1,2,3,9,6]
quick(arr, 0, len(arr)-1)
print(arr)