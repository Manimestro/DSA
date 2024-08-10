# find the element appears more then n/2 
arr=[3,3,4,3,8,8,3,3,3,3]
c=0
res = arr[0]
for i in range(len(arr)):
    if c==0:
        res=arr[i]
    if (arr[i]==res):
        c+=1
    else:
        c-=1
print(res)       
    