#Remove element from sorted array

def removeDuplicates(nums):
    i = 0
    k = 0
    while i < len(nums)-1:
        if nums[i] < nums[i+1]:
            i += 1
            k += 1
            nums[k] = nums[i]
        else:
            i += 1
    return k+1, nums


nums = [0,0,1,1,1,2,2,3,3,4]

k, arr = removeDuplicates(nums)

