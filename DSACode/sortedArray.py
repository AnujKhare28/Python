nums = [5,1,6,3,9,4,8,2]

nums2 = [1,1, 2, 3, 4, 5, 6, 8, 9]

def check_sorted(nums):

    for i in range(0,(len(nums) -1)):
        if nums[i] > nums[i + 1]:
            return False
    return True

print(check_sorted(nums2))

