# highest sum of subbray
arr=[-1,-2,-3,4,-1,5]
res = arr[0]
s=0
for i in range(len(arr)):
    if (s<0):
        s=0
    if (s>res):
        res=s
    s+=arr[i]
print(s)