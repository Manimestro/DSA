def sort(nums):
    l=m=0
    h=len(nums)-1
    while (m<=h):
        if nums[m]==0:
            temp = nums[m]
            nums[m] =nums[l]
            nums[l] = temp
            l+=1
            m+=1
        elif nums[m]==1:
            m+=1
        else :
            temp = nums[h]
            nums[h] =nums[m]
            nums[m] = temp
            h-=1
arr = [2,1,0,0,0,1,1,0,2]
sort(arr)
print(arr)