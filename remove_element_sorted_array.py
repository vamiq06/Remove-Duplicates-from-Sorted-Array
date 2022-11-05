#Remove element from sorted array
def removeDuplicates(nums):
    k = 1
    for i in range(len(nums)-1):
        if nums[i]==max(nums):
            break
        if nums[i]==nums[i+1]:
            nums.pop(i)
            nums.append(nums[i])
            i -= 1
        else:
            k += 1
    return k, nums

nums = [0,0,1,1,1,2,2,3,3,4]

k, arr = removeDuplicates(nums)

